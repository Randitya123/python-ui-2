from tkinter import*
from tkinter import messagebox
import time
s=Tk()
s.geometry("300x250")
h=StringVar()
m=StringVar()
s=StringVar()
h.set("00")
m.set("00")
s.set("00")
e1=Entry(s,width=3,textvariable=h)
e1.place(x=15,y=20)
s.mainloop()