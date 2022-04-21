from ast import excepthandler
from pkgutil import get_data
import tkinter
from tkinter import*

from tkinter import ttk,messagebox
import sqlite3

from PIL import*

class productclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x500+220+130')
        self.root.title("Medicine dashboard")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_pid=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()




        #==================================================
        product_Frame=Frame(self.root,bd=3,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=450,height=480)

        #=====title==========
        title=Label(product_Frame,text="Product details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        #==========column1===========
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18)).place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18)).place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=("goudy old style",18)).place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Side effects",font=("goudy old style",18)).place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text="Dosage",font=("goudy old style",18)).place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Prescription Req",font=("goudy old style",18)).place(x=30,y=310)

        #txt_category=Entry(product_Frame,text="Category",font=("goudy old style",18)).place(x=30,y=60)

        #===========column2===============
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER)
        cmb_cat.place(x=200,y=60,width=200)
        cmb_cat.current(0)


        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values= self.sup_list,state="readonly",justify=CENTER)
        cmb_sup.place(x=200,y=100,width=200)
        cmb_sup.current(0)


        txt_name=Entry(product_Frame,textvariable=self.var_name,bg="lightyellow").place(x=200,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,bg="lightyellow").place(x=200,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,bg="lightyellow").place(x=200,y=260,width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values= ("YES","NO"),state="readonly",justify=CENTER)
        cmb_status.place(x=200,y=310,width=200)
        cmb_status.current(0)

        #===================button=======================

        btn_add=Button(product_Frame,text="ADD",command=self.add,font=("goudy old style",10),bg="light green",fg="black",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="UPDATE",command=self.update,font=("goudy old style",10),bg="#2196f3",fg="black",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="DELETE",command=self.delete,font=("goudy old style",10),bg="red",fg="black",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="CLEAR",command=self.clear,font=("goudy old style",10),bg="light grey",fg="black",cursor="hand2").place(x=340,y=400,width=100,height=40)



        #=======================search frame==========================
        SearchFrame=LabelFrame(self.root,text="Search Medicine",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

 


        #================options===============
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values= ("Select","Category","Supplier","Name"),state="readonly",justify=CENTER)
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow").place(x=200,y=10)

        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",10),bg="blue",cursor="hand2").place(x=350,y=10,width=150,height=20)






         #======================Product Details==========================

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("pid",text="pid")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("name",text="name")
        self.product_table.heading("price",text="price")
        self.product_table.heading("qty",text="qty")
        self.product_table.heading("status",text="status")
        
        self.product_table["show"]="headings"

        
        
        self.product_table.column("pid",width=90)
        self.product_table.column("Category",width=90)
        self.product_table.column("Supplier",width=90)
        self.product_table.column("name",width=90)
        self.product_table.column("price",width=90)
        self.product_table.column("qty",width=90)
        self.product_table.column("status",width=90)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        


    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
            cur.execute("Select Name from category ")
            cat=cur.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            
            

            cur.execute("Select Name from supplier ")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)
        
            



        #================================add===============

    def add(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get=="Select" or self.var_name=="":
                messagebox.showerror("ERROR","ALL FIELDS MUST BE REQUIRED",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("ERROR","Name is already assigned",parent=self.root)
                    
                else:
                    cur.execute("Insert into product(Category,Supplier,name,price,qty,status)values(?,?,?,?,?,?)",(
                                                          self.var_cat.get(),
                                                          self.var_sup.get(),
                                                          self.var_name.get(),
                                                          self.var_price.get(),
                                                          self.var_qty.get(),
                                                          self.var_status.get(),
                                                           ))
                    con.commit()
                    messagebox.showinfo("Success","Product added",parent=self.root)
                    self.show()
                    


        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)


    def show(self):
         con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
         cur=con.cursor()

         try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

         except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

    def get_data(self,ev):
         f=self.product_table.focus()
         content=(self.product_table.item(f))
         row=content['values']
         self.var_pid.set(row[0])
         self.var_cat.set(row[1]),
         self.var_sup.set(row[2]),
         self.var_name.set(row[3]),
         self.var_price.set(row[4]),
         self.var_qty.set(row[5]),
         self.var_status.set(row[6]),

         



    


    #====================================================update=======================================
    def update(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("ERROR","Select a product",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","INVALID PRODUCT",parent=self.root)
                    
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                                         
                                                          self.var_cat.get(),
                                                          self.var_sup.get(),
                                                          self.var_name.get(),
                                                          self.var_price.get(),
                                                          self.var_qty.get(),
                                                          self.var_status.get(),
                                                          self.var_pid.get()
                                                          


                    ))
                    con.commit()
                    messagebox.showinfo("Update Success","Product Updated",parent=self.root)
                    self.clear()
                    

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

#================================delete=========================
    def delete(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
              if self.var_pid.get()=="":
                    messagebox.showerror("ERROR","Select Product",parent=self.root)
              else:
                    cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("ERROR","INVALID",parent=self.root)
                    
                    else:
                        op=messagebox.askyesno("CONFIRM","Do you really want to delete?",parent=self.root)
                        if op==True:
                             cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                             con.commit()
                             messagebox.showinfo("Delete","product deleted",parent=self.root)
                             self.clear()

        except Exception as ex:
                messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

     

          
            
#==================================clear======================
    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set(""),
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")  
        self.show()
    
#===========================search===================================
    def search(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()

        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select input should be required",parent=self.root)
            else:

                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%" +self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                         self.product_table.insert('',END,values=row)

                
                else:
                    messagebox.showerror("Error","NO record found",parent=self.root)
               

            
            

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

        
if __name__=="__main__":
        root = tkinter.Tk()
        obj = productclass(root)
        root.mainloop()