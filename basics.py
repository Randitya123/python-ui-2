#importing everthing from tkinter library
from tkinter import*
s=Tk()
s.geometry("1100x600")
s.config(background="black")
b1=Button(s,text="CLICK",background="gold",command=s.destroy).place(x=300,y=100)
#b1.pack()
#label
l1=Label(s,text="Randitya",font=("cambria",25),background="black",foreground="yellow").place(x=200,y=500)
c1=Entry(s,width=47,background="black",font=("cambria",25),foreground="yellow").place(x=100,y=300)
s.mainloop()