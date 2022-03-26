from password_generator import PasswordGenerator
from tkinter import *
from tkinter import messagebox

master=Tk()
master.title("Password Generator")
master.geometry("280x200")

password=PasswordGenerator()
password.minlen=10
password.maxlen=15
password.minuchars=1
password.minlchars=1

def passgen():
    delete()
    res=password.generate()
    pw.insert(0,res)

def delete():
    pw.delete(0,END)

pw=Entry(master)
pw.grid(row=1,column=0,ipady=10,ipadx=30)

label1=Label(master,text="Password Generator",font="Arial 15 underline")
label1.grid(row=0, column=0,ipadx=50)

button1=Button(master,text="Generate Password",bg="black", fg="white",command=passgen)
button1.grid(row=3,column=0,ipady=5,ipadx=5)

button1=Button(master,text="Delete",bg="black", fg="white",command=delete)
button1.grid(row=4,column=0,ipady=5,ipadx=5)

button2=Button(master,text="EXIT",bg="grey", fg="white",command=master.quit)
button2.grid(row=5,column=0,ipady=0,ipadx=5)

master.mainloop()