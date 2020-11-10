#sell page
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
def sell():
    if(conn): 
        if(var1.get()=="" or var2.get()=="" or var3.get()=="" or var3.get().isnumeric()==False):
                messagebox.showerror("showerror", "Enter correct Value")
        else:
            mycs=conn.cursor()
            cmd="SELECT * FROM books WHERE ID='"+var1.get()+"'"
            mycs.execute(cmd)
            result=mycs.fetchall()
            if(result!=[]):
                messagebox.showerror("showerror", "Enter Different ID")
                result=[]
            else:
                mycs=conn.cursor()
                cmd="INSERT INTO books (ID,BookName,Price) VALUES (%s, %s,%s)"
                val=(var1.get(),var2.get(),var3.get())
                mycs.execute(cmd,val)
                conn.commit()
                top=Tk()
                top.geometry("400x400")
                top.title("Book uploaded for sale")
                l2=Label(top,text="Thank you for choosing us to sell your books.Your book has been displayed for sale")
                l2.grid(row=0,column=0)
                b=Button(top,text="Exit",command=quit)
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
b=Button(top,text="submit",command=sell)
b.grid(row=3,column=1)
l3=Label(top)
l3.grid(row=3,column=0)
top.mainloop()
