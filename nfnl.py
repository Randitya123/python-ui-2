from tkinter import*
from tkinter.ttk import*
from time import strftime
s=Tk()
s.config(background="pink") 
s.title("Clock")
def function():
    string=strftime('%H:%M:%S %p')
    l1.config(text=string)
    l1.after(1000,function)
l1=Label(s,font=("arial",50),background="Pink",foreground="Light Blue")
l1.place(x=100,y=100)
function()
s.mainloop()