from cgitb import text
from email.mime import image
import imp
from logging import root
from tkinter import*
from tkinter import font
from turtle import title, width
from PIL import ImageTk
from tkinter import messagebox
class Login_Sysytem:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System |  Developed by Group5 (G5)")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #===images===
        self.phone_image=ImageTk.PhotoImage(file="images/icon.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)


        #===Login_frame===
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        #do change here (SM)
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white",fg="black").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Username",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.username,font=("times new roman",15),bg="#ECECEC",fg="black").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC",fg="black").place(x=50,y=240,width=250)

        #do change here (SM)
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)


        #===Frame2===
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Don't have an account ?",font=("times new roman",13),bg="white",fg="black").place(x=40,y=20)
        btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=200,y=17)

        #===Animation Images===
        self.im1=ImageTk.PhotoImage(file=("images/im1.jpeg"))
        self.im2=ImageTk.PhotoImage(file=("images/im2.jpeg"))
        self.im3=ImageTk.PhotoImage(file=("images/im3.jpeg"))
    
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
   
        self.animate()
    
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)

    
    
    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All Fields are required")
        
        elif self.username.get()!="Shreyan" or self.password.get()!="123456":
            messagebox.showerror("Error", "Invalid Username or Password\nTry again with correct credentials")

        else:
            messagebox.showinfo("Information",f"Welcome: {self.username.get()}\nYour Password: {self.password.get()}")





root=Tk()
obj=Login_Sysytem(root)
root.mainloop()