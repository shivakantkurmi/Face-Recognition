from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img3 = Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=50,width=1530,height=710)

        dev_label = Label(bg_img, text="Email: shivakantkurmi49@gmail.com", font=("times new roman",20,"bold"),bg="blue",fg="white")
        dev_label.place(x=550,y=200 )

       

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()