from tkinter import *
from tkinter import ttk
import tkinter 
from PIL import Image, ImageTk
from student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help
from face_recognition import Face_Recognition
import os
from time import strftime

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root


        imgs = Image.open(r"img/vit2.jpeg")
        imgs = imgs.resize((530,150),Image.LANCZOS)
        self.photoimgs = ImageTk.PhotoImage(imgs)
        f_lbl = Label(self.root,image = self.photoimgs)
        f_lbl.place(x=0,y=0,width=530,height=150)




        imgl = Image.open(r"img/vit2.jpeg")
        imgl = imgl.resize((530,150),Image.LANCZOS)
        self.photoimgl = ImageTk.PhotoImage(imgs)
        f_lbl = Label(self.root,image = self.photoimgl)
        f_lbl.place(x=1060,y=0,width=530,height=150)




        #background image
        img3 = Image.open(r"img\bg.jpg")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)


        #img 1
        img = Image.open(r"img\vit.jpg")
        img = img.resize((530,150),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=530,y=0,width=530,height=150)




        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        #student button
        img4 = Image.open(r"img\details.jpeg")
        img4 = img4.resize((220,220),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image = self.photoimg4, command=self.student_details ,cursor="hand2")
        b1.place(x=200,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details ,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=260,width=220,height=40)


        #train button
        img8 = Image.open(r"img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img8 = img8.resize((220,220),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image = self.photoimg8, command=self.train_data,cursor="hand2")
        b1.place(x=500,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Train Face", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=260,width=220,height=40)

        #detect face button
        img5 = Image.open(r"img\face_detector1.jpg")
        img5 = img5.resize((220,220),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image = self.photoimg5,command=self.face_date, cursor="hand2")
        b1.place(x=800,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_date,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=260,width=220,height=40)


        #attendance button
        img6 = Image.open(r"img\smart-attendance.jpg")
        img6 = img6.resize((220,220),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image = self.photoimg6, command=self.attendance_date, cursor="hand2")
        b1.place(x=1100,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_date,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=260,width=220,height=40)


        

        #photos button
        img9 = Image.open(r"img\student.jpg")
        img9 = img9.resize((220,220),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image = self.photoimg9, command=self.open_img,cursor="hand2")
        b1.place(x=200,y=350,width=220,height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=560,width=220,height=40)

        
        
        #developer button
        img10 = Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img10 = img10.resize((220,220),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,command=self.developer_date ,image = self.photoimg10, cursor="hand2")
        b1.place(x=500,y=350,width=220,height=220)

        b1_1 = Button(bg_img,command=self.developer_date, text="Developer", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=560,width=220,height=40)



        #helpdesk button
        img7 = Image.open(r"img\help.jpg")
        img7 = img7.resize((220,220),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, command=self.help_date ,image = self.photoimg7, cursor="hand2")
        b1.place(x=800,y=350,width=220,height=220)

        b1_1 = Button(bg_img, text="Help Desk", command=self.help_date,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=560,width=220,height=40)


        #exit button
        img11 = Image.open(r"img\exit.jpg")
        img11 = img11.resize((220,220),Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,command=self.iExit, image = self.photoimg11, cursor="hand2")
        b1.place(x=1100,y=350,width=220,height=220)

        b1_1 = Button(bg_img,command=self.iExit ,text="Exit", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=560,width=220,height=40)

        # ======== functions buttons ==========


    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()