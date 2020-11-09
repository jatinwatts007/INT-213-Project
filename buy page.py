#buy page
import mysql.connector
from functools import partial
from tkinter import *
from tkinter import messagebox
conn = mysql.connector.connect( 
      host ="localhost", 
      user ="cse213",
      passwd="jatin@007",
        database="geeks4geeks"
    )
def quit():
    top.destroy()
def val():
    if(conn):
        if(var1.get()=="" or var2.get()==""):
            messagebox.showerror("showerror", "Enter Value")
        else:
            mycs=conn.cursor()
            cmd="SELECT * FROM books WHERE ID='"+var1.get()+"'"
            mycs.execute(cmd)
            result=mycs.fetchall()
            if(result==[]):
                messagebox.showinfo("showinfo", "Enter correct ID")
            else:
                mycs=conn.cursor()
                cmd="DELETE FROM books WHERE ID=%s"
                mycs.execute(cmd,(var1.get(),))
                conn.commit()
                cmd="INSERT INTO buydata (ID,Address) VALUES (%s, %s)"
                val=(var1.get(),var2.get())
                mycs.execute(cmd,val)
                conn.commit()
                top=Tk()
                top.geometry("400x400")
                top.title("Sales Management System")
                l1=Label(top,text="Thank you for buying")
                l1.grid(row=0,column=0)
                b=Button(top,text="exit",command=quit)
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
l1=Label(top,text="Enter delivery address")
l1.grid(row=1,column=0)
e1=Entry(top,bd=5,textvariable=var2)
e1.grid(row=1,column=1)
b=Button(top,text="buy",command=val)
b.grid(row=2,column=1)
l1=Label(text="online payment")
l1.grid(row=4,column=0)
l1=Label(text="Phone no:-9610830608")
l1.grid(row=5,column=0)
l1=Label(text="(Any app)")
l1.grid(row=6,column=0)
top.mainloop()
