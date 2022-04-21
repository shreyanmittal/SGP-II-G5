'''
from ast import excepthandler
from pkgutil import get_data
from sre_constants import IN
from tkinter import*
import tkinter
from tkinter import*
import sqlite3
'''
from ast import excepthandler
from pkgutil import get_data
from tkinter import*
import tkinter
from tkinter import ttk,messagebox
import sqlite3
from PIL import Image,ImageTk

class categoryclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1200x500+220+130')
        self.root.title("Category")
        self.root.config(bg="white")
        self.root.focus_force()

        #===========variabl====
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #=========title==============
        lbl_title=Label(self.root,text="Manage Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text="Enter Category",font=("goudy old style",18),bg="white").place(x=50,y=100)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20),bg="lightyellow").place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)

        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)


        #===============CATEGORY DETAILS================================

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,height=100,width=380)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categorytable=ttk.Treeview(cat_frame,columns=("cid","Name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categorytable.xview)
        scrolly.config(command=self.categorytable.yview)
        self.categorytable.heading("cid",text="C ID")
        self.categorytable.heading("Name",text="Name")
        
        self.categorytable["show"]="headings"

        self.categorytable.column("cid",width=90)
        self.categorytable.column("Name",width=90)
        self.categorytable.pack(fill=BOTH,expand=1)
        self.categorytable.bind("<ButtonRelease-1>",self.get_data)


        #==============image==============
        
        self.im1=Image.open("images/cat1.jpg")
        self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)




        self.im2=Image.open("images/cat2.jpg")
        self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        
        self.show()
    #==============add=====================
    def add(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("ERROR","CATEGORY NAME MUST BE REQUIRED",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("ERROR","Category is already present",parent=self.root)
                    
                else:
                    cur.execute("Insert into category(Name)values(?)",(
                                                          self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","category added",parent=self.root)
                    self.show()
                    


        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)



    def show(self):
         con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
         cur=con.cursor()

         try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categorytable.delete(*self.categorytable.get_children())
            for row in rows:
                self.categorytable.insert('',END,values=row)

         except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

    def get_data(self,ev):
         f=self.categorytable.focus()
         content=(self.categorytable.item(f))
         row=content['values']
         #print(row)
         self.var_cat_id.set(row[0])
         self.var_name.set(row[1])
  #===============================delete============

    def delete(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
              if self.var_cat_id.get()=="":
                    messagebox.showerror("ERROR","PLEASE SELECT CATEGORY",parent=self.root)
              else:
                    cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("ERROR","TRY AGAIN",parent=self.root)
                    
                    else:
                        op=messagebox.askyesno("CONFIRM","Do you really want to delete?",parent=self.root)
                        if op==True:
                             cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                             con.commit()
                             messagebox.showinfo("Delete","Category deleted",parent=self.root)
                             self.show()
                             self.var_cat_id.set("")
                             self.var_name.set("")

        except Exception as ex:
                messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

     

        



        

if __name__=="__main__":
        root = tkinter.Tk()
        obj = categoryclass(root)
        root.mainloop()