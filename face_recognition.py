from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import csv
host = "127.0.0.1"
username = "root"
password = "250805"
database = "face_recognition_system"

import os
import numpy as np



import csv
import mysql.connector
from datetime import datetime
import os






















class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #image left
        img_top = Image.open(r"img\face_detector1.jpg")
        img_top = img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label( self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #image right
        img_side = Image.open(r"img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_side = img_side.resize((950,700),Image.LANCZOS)
        self.photoimg_side = ImageTk.PhotoImage(img_side)

        f_lbl = Label(self.root,image = self.photoimg_side)
        f_lbl.place(x=650,y=55,width=950,height=700)

        #button
        b1_1 = Button(f_lbl, text="Face Detection",command=self.face_recog, cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=370,y=615,width=200,height=40)

        students = self.fetch_students_from_database()
        
        # Create or update the attendance CSV file for today
        self.create_attendance_csv(students)




    def fetch_students_from_database(self):
            # Connect to the MySQL database
        
            connection = mysql.connector.connect(
                host=host,
                user=username,
                password=password,
                database=database
            )
        
            # Create a cursor object to execute queries
            cursor = connection.cursor()
        
            # Fetch student data from the database
            cursor.execute("SELECT student_id, roll, dep, name FROM student")
        
            # Fetch all records
            students = cursor.fetchall()
        
            # Close the cursor and connection
            cursor.close()
            connection.close()
            return students
        
        
    def is_today_data_exist(self,csv_file, today_date):
            # Check if today's date exists in the CSV file
            with open(csv_file, "r") as file:
                reader = csv.reader(file)
                # next(reader)  # Skip the header row
                for row in reader:
                    if row[4] == today_date:
                        return True
            return False
        
        
        
    def create_attendance_csv(self,students):
            # Get today's date
            today_date = datetime.now().strftime("%d/%m/%y")
        
            # Check if attendance data for today already exists in the CSV file
            if not os.path.isfile("attendance.csv") or not self.is_today_data_exist("attendance.csv", today_date):
                # Create a list to hold the data for all students
                student_data = []
        
                # Append data for each student with default attendance status as "Absent" and today's date
                for student in students:
                    student_data.append([student[0], student[1], student[3], student[2], today_date, "Absent"])
        
                # Write the data to a CSV file
                with open("attendance.csv", "a", newline="\n") as file:
                    # Create a CSV writer object
                    writer = csv.writer(file)
                    writer.writerow(["","","","",today_date,""])
                    writer.writerows(student_data)  # Write the student data
        
                print("Attendance CSV file created/updated successfully.")
        
            else:
                # Check if each student is already present in today's attendance data
                with open("attendance.csv", "r") as file:
                    existing_data = [row[0] for row in csv.reader(file)]
                
                # Append data for students not already present in today's attendance data
                new_student_data = []
                for student in students:
                    if student[0] not in existing_data:
                        new_student_data.append([student[0], student[1], student[3], student[2], today_date, "Absent"])
        
                if new_student_data:
                    with open("attendance.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(new_student_data)
                    print("New student data added to attendance CSV file.")
        
                else:
                    print("Attendance CSV file for today already exists. No changes made.")
        
        
        

        
        





 
     #========atendance=============

    def mark_attendance(self,id, r,n):
        now = datetime.now()
        c_d = now.strftime("%d/%m/%Y")
        detected = False  # Flag to track if student is detected and attendance is marked
    
        with open("attendance.csv", "r") as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
    
        # Check if student's data matches with any row in the CSV file
        for i, row in enumerate(rows):
            if row[5]=="Absent" and id==row[0] :
                # If match found, mark attendance as "Present"
                rows[i][5] = "Present"
                detected = True
                print("Attendance marked as 'Present' for student:", n)
                break
    
        # If student not detected, print a message
        if not detected:
            # print("Student not detected. Attendance not marked.")
            pass
    
        # Write updated data back to CSV file
        with open("attendance.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)
    











    #========face recognition=======
    def face_recog(self):
            now = datetime.now()
            c_d = now.strftime("%d/%m/%Y")
            if self.is_today_data_exist("attendance.csv",c_d):
                 # Open the CSV file in append mode
                 with open("attendance.csv", "a", newline="") as file:
                     # Write a new line to the file
                     file.write("\n\n")

            def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,tex,clf):
                gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

                coord = []
                # alldata=[]

                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                    confidence = int((100*(1-predict/300)))

                    conn = mysql.connector.connect(
                        host=host,
                        user=username,
                        password=password,
                        database=database,
                        auth_plugin='mysql_native_password'
                    )
                    my_cursor = conn.cursor()

                    my_cursor.execute("select name from student where student_id ="+str(id))
                    n = my_cursor.fetchone()
                    n ="+".join(n)

                    my_cursor.execute("select roll from student where student_id ="+str(id))
                    r = my_cursor.fetchone()
                    r ="+".join(r)

                    my_cursor.execute("select dep from student where student_id ="+str(id))
                    d = my_cursor.fetchone()
                    d ="+".join(d)

                    my_cursor.execute("select student_id from student where student_id ="+str(id))
                    i = my_cursor.fetchone()
                    i ="+".join((i))
#here error founded
                    if confidence > 73:
                        # cv2.putText(img, f"ID:{i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(150,255,0),3)
                        cv2.putText(img, f"Reg. No:{r}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(230,0,0),3)
                        cv2.putText(img, f"Name:{n}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.7,(40,250,00),3)
                        # cv2.putText(img, f"Department:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(40,250,00),3)
                        self.mark_attendance(i,r,n)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img, "Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord = [x,y,w,h]
                return coord
            
            def recognize(img,clf,faceCascade):
                coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
                return img
            
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")


            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                img = recognize(img,clf,faceCascade)
                cv2.imshow("Welcome to face recognition",img)


                if cv2.waitKey(1) == 13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()    




if __name__ == "__main__":
    root = Tk() 
    obj = Face_Recognition(root)
    root.mainloop()