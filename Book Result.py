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
    b=Button(top,text="BUY")
    b.grid(row=i+4,column=2)
    b=Button(top,text="SELL")
    b.grid(row=i+4,column=3)
def quit():
    top.destroy()
top=Tk()
top.geometry("300x300")
top.title("Sales Management System")
b=Button(top,text="BOOKLIST",command=Bookresult)
b.place(relx=0.5, rely=0.5, anchor=CENTER)
b=Button(top,text="EXIT",command=quit)
b.grid(row=0,column=0)
top.mainloop()
