import sqlite3
def create_db():
    con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS medicine(Medicine_ID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Company text,Type text,Price text,Quantity text,Manufacturing_Date text,Expiry_Date text)")
    con.commit()
    

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,contact text,description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS dosage(invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,contact text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,name text,price text,qty text,status text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    
    

    




    


create_db()