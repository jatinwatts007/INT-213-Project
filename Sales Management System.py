import mysql.connector  
from tkinter import *
conn = mysql.connector.connect( 
  host ="localhost", 
  user ="cse213",
  passwd="jatin@007"
) 
  
# preparing a cursor object 
cursorObject = conn.cursor() 
  
# creating database 
cursorObject.execute("CREATE DATABASE SALEES MANAGEMENT SYSTEM")

userRecord = "CREATE TABLE USER( NAME varchar(20) NOT NULL, PASSWORD varchar(50) UNIQUE)"

# table created 
cursorObject.execute(userRecord)

BookRecord = "CREATE TABLE Books (ID varchar(255) NOT NULL UNIQUE,BookName varchar(255) NOT NULL,Price varchar(255) NOT NULL);"

# table created 
cursorObject.execute(BookRecord)

def insert():  
    mycursor = conn.cursor()
    sql = "INSERT INTO books (ID,BookName,Price) VALUES (%s, %s,%s)"
    
    val = ("4","CSE320 Software Engineering","585")
      
    mycursor.execute(sql, val) 
    conn.commit()
    

   
   
   
def aboutus():
    top=Tk()
    top.geometry("400x400")
    top.title("About Us")
    l1=Label(top,text="Sales Management System of used books")
    l1.grid(row=0,column=2)
    l1=Label(top,text="Poject INT 213")
    l1.grid(row=1,column=2)
    l1=Label(top,text="Made By: Jatin Watts")
    l1.grid(row=2,column=2)
    l1=Label(top,text="Submitted to Pooja Rana")
    l1.grid(row=3,column=2)
    l1=Label(top,text="System that helps in buying and selling books")
    l1.grid(row=4,column=2)
    top.mainloop()    


    
def logout():
    def logout1():
        top=Tk()
        top.geometry("300x300")
        top.title("Logout")
        label = Label(top, text=" Sucessfully Logout Press Ok to go to Login Page")
        label.grid(row=0,column=0)
        b=Button(top,text="ok")
        
        b.grid(row=1,column=0)
        top.mainloop()
    b=Button(root,text="Logout",command=logout1)
    b.grid(row=2,column=1)
    root.mainloop()
    
    
def BUY():                                      
    def val():
        mycs=conn.cursor()
        cmd="DELETE FROM books WHERE ID=%s"
        mycs.execute(cmd,(var1.get(),))
        conn.commit()
        top=Tk()
        top.geometry("400x400")
        top.title("Sales Management System")
        l1=Label(top,text="Thank you for buying")
        l1.grid(row=0,column=0)
        b=Button(top,text="logout",command=logout)
        b.grid(row=2,column=1)
        top.mainloop()
    top=Tk()
    top.geometry("400x400")
    top.title("Payment Page")
    var1=StringVar()
    l1=Label(top,text="Enter Book ID")
    l1.grid(row=0,column=0)
    e1=Entry(top,bd=5,textvariable=var1)
    e1.grid(row=0,column=1)
    b=Button(top,text="buy",command=val)
    b.grid(row=2,column=1)
    l1=Label(text="online payment")
    l1.grid(row=4,column=0)
    l1=Label(text="Phone no:-9610830608")
    l1.grid(row=5,column=0)
    l1=Label(text="(Any app)")
    l1.grid(row=6,column=0)
    top.mainloop()
    
def SELL():
    def val():
        if(conn):
            mycs=conn.cursor()
            cmd="INSERT INTO books (ID,BookName,Price) VALUES (%s, %s,%s)"
            val=(var1.get(),var2.get(),var3.get())
            mycs.execute(cmd,val)
            mydb.commit()
            top=Tk()
            top.geometry("400x400")
            top.title("Book uploaded for sale")
            l2=Label(top,text="Thank you for choosing us to sell your books.Your book has been displayed for sale")
            l2.grid(row=0,column=0)
            b=Button(top,text="logout",command=logout)
            b.grid(row=1,column=0)
            top.mainloop()
    top=Tk()
    top.geometry("400x400")
    top.title("Book upload for sale")
    var1,var2,var3=StringVar(),StringVar(),StringVar()
    l1=Label(top,text="Enter Book ID")
    l1.grid(row=0,column=0)
    e1=Entry(top,bd=5,textvariable=var1)
    e1.grid(row=0,column=1)
    l2=Label(top,text="Enter BookName")
    l2.grid(row=1,column=0)
    e2=Entry(top,bd=5,textvariable=var2)
    e2.grid(row=1,column=1)
    l2=Label(top,text="Enter BookPrice")
    l2.grid(row=2,column=0)
    e3=Entry(top,bd=5,textvariable=var3)
    e3.grid(row=2,column=1)
    b=Button(top,text="submit",command=val)
    b.grid(row=3,column=1)
    l3=Label(top)
    l3.grid(row=3,column=0)
    top.mainloop()
    
    
    
def Bookresult():
    top=Tk()
    top.geometry("600x600")
    top.title("BookList")
    cursor = conn.cursor()
    cursor.execute( " SELECT * FROM books ")
    # fetch all of the rows from the query
    data = cursor.fetchall ()
    
    # print the rows
    i=0
    for row in data :
        l=Label(top,text="ID =")
        l.grid(row=i,column=0)
        l1=Label(top,text= row[0])
        l1.grid(row=i,column=1)
        l3=Label(top,text="BookName =")
        l3.grid(row=i,column=2)
        l4=Label(top,text= row[1])
        l4.grid(row=i,column=3)
        l=Label(top,text="Price =")
        l.grid(row=i,column=5)
        l1=Label(top,text= row[2])
        l1.grid(row=i,column=7)
        i=i+1;
    b=Button(top,text="BUY",command=BUY)
    b.grid(row=i+4,column=2)
    b=Button(top,text="SELL",command=SELL)
    b.grid(row=i+4,column=3)
    top.mainloop()
    
    
def booklist button():
    top=Tk()
    top.geometry("300x300")
    top.title("Sales Management System")
    b=Button(top,text="BOOKLIST",command=Bookresult)
    b.place(relx=0.5, rely=0.5, anchor=CENTER)
    top.mainloop()
    
    
def signin():
   def val():
       mydb=mysql.connector.connect(host="localhost",user="cse213",
                                    password="jatin@007",database="geeks4geeks")
       if(mydb):
           mycs=mydb.cursor()
           cmd="INSERT INTO user (NAME,PASSWORD) VALUES (%s, %s)"
           val=(var1.get(),var2.get())
           mycs.execute(cmd,val)
           mydb.commit()
   top=Tk()
   top.geometry("400x400")
   top.title("Sigin form")
   var1,var2=StringVar(),StringVar()
   l1=Label(top,text="Enter Name")
   l1.grid(row=0,column=0)
   e1=Entry(top,bd=5,textvariable=var1)
   e1.grid(row=0,column=1)
   l2=Label(top,text="Enter Password")
   l2.grid(row=1,column=0)
   e2=Entry(top,bd=5,textvariable=var2)
   e2.grid(row=1,column=1)
   b=Button(top,text="Login",command=val)
   b.grid(row=2,column=1)
   l3=Label(top)
   l3.grid(row=3,column=0)
   top.mainloop()
 
def login():
    def val():
        if(conn):
            mycs=conn.cursor()
            cmd="SELECT * FROM user WHERE NAME='"+var1.get()+"' AND PASSWORD='"+var2.get()+"'"
            mycs.execute(cmd)
            result=mycs.fetchall()
            if(result==[]):
                l3.config(text="Not valid user",font=("Times New Roman",15),bg="red")
            else:
                l3.config(text="valid user",font=("Times New Roman",15),bg="green")
            booklist button()
    top=Tk()
    top.geometry("400x400")
    top.title("Login form")
    var1,var2=StringVar(),StringVar()
    l1=Label(top,text="Enter Name")
    l1.grid(row=0,column=0)
    e1=Entry(top,bd=5,textvariable=var1)
    e1.grid(row=0,column=1)
    l2=Label(top,text="Enter Password")
    l2.grid(row=1,column=0)
    e2=Entry(top,bd=5,textvariable=var2,show="*")
    e2.grid(row=1,column=1)
    b=Button(top,text="Login",command=val)
    b.grid(row=2,column=1)
    l3=Label(top)
    l3.grid(row=3,column=0)
    top.mainloop() 

top=Tk()
top.geometry("300x300")
top.title("Sales Management System")
b=Button(top,text="Login",command=login)
b.grid(row=0,column=1)
b=Button(top,text="Signup",command=signin)
b.grid(row=0,column=3)
b=Button(top,text="About Us",command=aboutus)
b.grid(row=0,column=5)
top.mainloop()
