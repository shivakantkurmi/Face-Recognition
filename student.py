from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
host = "127.1"   #change with you mysql details
username = "root"    #change with you mysql details
password = "2505"    #change with you mysql details
database = "face_recognition_system"    #change with you mysql details







class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")  


        #=============== variables =================

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()








        #img 1
        img = Image.open(r"img\std.jpeg")
        img = img.resize((1530,150),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=150)


        # # img2
        # imgs = Image.open(r"img/s1.png")
        # imgs = imgs.resize((630,130),Image.LANCZOS)
        # self.photoimgs = ImageTk.PhotoImage(imgs)
        # f_lbl = Label(self.root,image = self.photoimgs)
        # f_lbl.place(x=800,y=0,width=630,height=130)


         #background image
        img3 = Image.open(r"img\dev.jpg")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=10,width=1500,height=600)

        #left  label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=1,width=730,height=590)

        img_left = Image.open(r"img\girl.jpeg")
        img_left = img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label( Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

                #current course
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=130)

                            #department
        dep_label = Label(current_course_frame, text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10, sticky=W )

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep ,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"] = ("Select Department","B.Tech CSE","B.Tech CSE (Gaming Technology)","B.Tech CSE (Cyber security )","int. M.Tech (data science)",
                               "B.Tech CSE (Cloud computing)","Bio Engineering","B.Tech CSE (E-Commerce Technology)","B.Tech ECE",
                               "B.Tech ECE (AI & Cybernetics)","CSE (ai and ml)","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W) 


                            #course
        course_label = Label(current_course_frame, text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10, sticky=W )

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"] = ("Select Course","CSA1002","CSA2001-Fundamentals of AI and ML",
                                  "CSE2001 OOP's with C++ ","CSE2002 DSA"," EEE1001  ",
                                  " CSE2006 Programming in Java","CET3012 Gaming for Education"
                                  ," CSE3003 Operating Systems",
                                  "SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W) 


                            #year
        year_label = Label(current_course_frame, text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10, sticky=W ) 

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)  
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 


                            #semester
        semester_label = Label(current_course_frame, text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10, sticky=W )

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"] = ("Select Semester","Winter semester 2024","Fall Semester 2024","Fall inter Semester-1")
        semester_combo.current(0)  
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 


        #Class student information
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=265,width=720,height=300)

                         #stidentId
        studentId_label = Label(class_student_frame, text="CLASS ROLL NO:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10, pady=5, sticky=W )

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10, pady=5, sticky=W)


                        #student name
        studentName_label = Label(class_student_frame, text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10, pady=5, sticky=W )

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10, pady=5, sticky=W)


                         #class
        class_div_label = Label(class_student_frame, text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10, pady=5, sticky=W )

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"] = ("A","B","C")
        div_combo.current(0)  
        div_combo.grid(row=1,column=1,padx=10, pady=5, sticky=W) 

                        #roll no
        roll_no_label = Label(class_student_frame, text="Registration No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10, pady=5, sticky=W )

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5, sticky=W)


                        #gender
        gender_label = Label(class_student_frame, text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10, pady=5,sticky=W )

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)  
        gender_combo.grid(row=2,column=1,padx=10, pady=5,sticky=W) 


                        #dob
        dob_label = Label(class_student_frame, text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10, pady=5,sticky=W )

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


                        #email
        email_label = Label(class_student_frame, text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5, sticky=W )

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5, sticky=W)


                        #phone no
        phone_label = Label(class_student_frame, text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5, sticky=W )

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5, sticky=W)


                         #address
        address_label = Label(class_student_frame, text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5, sticky=W )

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5, sticky=W)


                         #teacher name
        teacher_label = Label(class_student_frame, text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5, sticky=W )

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5, sticky=W)


        #radio buttons
        self.var_radios1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radios1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radios1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=705,height=70)

        save_btn = Button(btn_frame, text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_date,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)

        take_photo_btn = Button(btn_frame, text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn = Button(btn_frame, text="Update Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        update_photo_btn.grid(row=1,column=1)

        
        # # back button
        # bc_btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        # bc_btn_frame.place(x=10,y=200,width=705,height=770)
        # back_btn = Button(bc_btn_frame, text="Back",command=main.Main(),font=("times new roman",12,"bold"),bg="red",fg="white",width=19)
        # back_btn.grid(row=10,column=0)

        


        #right  label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=1,width=720,height=590)

        img_right = Image.open(r"img\student.jpg")
        img_right = img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label( Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        # ==========search system============

        search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE,text="Search",font=("times new roman",12,"bold"),bg="white")
        search_frame.place(x=5,y=135,width=710,height=70 )

        search_label = Label(search_frame, text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10, pady=5, sticky=W )

        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"] = ("Select","Roll","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W) 


        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width=14)
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn = Button(search_frame, text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white",width=14)
        showAll_btn.grid(row=0,column=4,padx=4 )

        #============table frame=============
        tabel_frame = Frame(Right_frame, bd=2, relief=RIDGE,bg="white")
        tabel_frame.place(x=5,y=210,width=710,height=350)

 
        scroll_x = ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(tabel_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="class Roll no")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Registration No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    #============== function declaration ============

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required!!!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host=host,
                    user=username,
                    password=password,
                    database=database,
                    auth_plugin='mysql_native_password'
                )
                my_cursor = conn.cursor()
                my_cursor.execute(("INSERT INTO student (dep, course, year, semester, student_id, name, division, roll, gender, dob, email, phone, address, teacher, photoSample) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
,                           (
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_id.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radios1.get()
                            ))
                            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #===========fetch data==============
    def fetch_data(self):
        conn = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database,
        auth_plugin='mysql_native_password'
         )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    #=========get cursor===============
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radios1.set(data[14])



    #==========update function==========
    def update_date(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required!!!",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you wand to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(
                            host=host,
                            user=username,
                            password=password,
                            database=database,
                            auth_plugin='mysql_native_password'
                        )
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radios1.get(),
                        self.var_std_id.get(),
                    ))
                else:
                    if not Update:
                        return
                
                messagebox.showinfo("Success","Student details successfully updated.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=============delete function===========
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete","Do you wand to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                            host=host,
                            user=username,
                            password=password,
                            database=database,
                            auth_plugin='mysql_native_password'
                        )
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details successfully deleted.", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=========reset function============
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radios1.set("")


    #=============generate dataset & take photo sample============
#     def generate_dataset(self):
#         if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
#             messagebox.showerror("Error", "All Fields are required!!!",parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(
#                     host=host,
#                     user=username,
#                     password=password,
#                     database=database,
#                     auth_plugin='mysql_native_password'
#                 )
#                 my_cursor = conn.cursor() 
#                 my_cursor.execute("select * from student")
#                 myresult = my_cursor.fetchall()
#                 id=0
#                 for x in myresult:
#                     id+=1
#                 my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where student_id=%s",(
#                         self.var_dep.get(),
#                         self.var_course.get(),
#                         self.var_year.get(),
#                         self.var_semester.get(),
#                         self.var_std_name.get(),
#                         self.var_div.get(),
#                         self.var_roll.get(),
#                         self.var_gender.get(),
#                         self.var_dob.get(),
#                         self.var_email.get(),
#                         self.var_phone.get(),
#                         self.var_address.get(),
#                         self.var_teacher.get(),
#                         self.var_radios1.get(),
#                         self.var_std_id.get() 
#                     ))
#                 id = self.var_std_id.get() 
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close()

#                 #=============load predefined data on face frontal from opencv============

#                 face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#                 def face_cropped(img):
#                     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                     faces = face_classifier.detectMultiScale(gray,1.3,5)
#                     #scaling factor=1.3
#                     #Minimum neighbour=5

#                     for (x,y,w,h) in faces:
#                         face_cropped = img[y:y+h, x:x+w]
#                         return face_cropped
#                 cap = cv2.VideoCapture(0)
#                 img_id=0
#                 while True:
#                     ret,my_frame = cap.read()
#                     if face_cropped(my_frame) is not None:
#                         img_id+=1
#                         face = cv2.resize(face_cropped(my_frame),(350,350))
#                         face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
#                         file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
#                         cv2.imwrite(file_name_path,face)
#                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
#                         cv2.imshow("Cropped Face", face)
#                     if cv2.waitKey(1) == 13 or int(img_id) == 500:  #no. of images
#                         break
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo("Result","Generating data sets completed!!!",parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)








# if __name__ == "__main__":
#     root = Tk()
#     obj = Student(root)
#     root.mainloop()

















        
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required!!!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host=host,
                    user=username,
                    password=password,
                    database=database,
                    auth_plugin='mysql_native_password'
                )
                my_cursor = conn.cursor() 
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radios1.get(),
                        self.var_std_id.get() 
                    ))
                id = self.var_std_id.get() 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                if face_cascade.empty():
                    messagebox.showerror("Error", "Unable to load the Haar cascade classifier.")
                    return
                
                cap = cv2.VideoCapture(0)  
                if not cap.isOpened():
                    messagebox.showerror("Error", "Unable to access the webcam.")
                    return
                
                save_dir = "data"
                existing_files = os.listdir(save_dir)
                existing_ids = [int(file.split('.')[1]) for file in existing_files if file.startswith('user.')]
                user_id = id
                
                img_id = 0
                
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to retrieve frame from the webcam.")
                        break
                    
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    
                    for (x, y, w, h) in faces:
                        cropped_face = frame[y:y+h, x:x+w]
                        img_id += 1
                        file_name_path = os.path.join(save_dir, f"user.{user_id}.{img_id}.jpg")
                        cv2.imwrite(file_name_path, cropped_face)
                        cv2.putText(frame, str(img_id), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    
                    cv2.imshow("Collecting Dataset", frame)
                    
                    if cv2.waitKey(1) == 13 or img_id == 500:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Collecting samples for user " + str(user_id) + " is completed.")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
