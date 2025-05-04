from tkinter import*
from tkinter.filedialog import*
screen=Tk()
screen.configure(bg="black")
l1=Label(screen,text="My Adress Book",fg="WHITE")
l1.grid(row=0,column=1,pady=10, columnspan=3)

b1=Button(screen,text="OPEN",background="BLACK",fg="WHITE")
b1.grid(row=0,column=3,pady=10)

list1=Listbox(screen,height=15,width=30)
list1.grid(row=2,column=0)

l2=Label(screen,text="Name",background="BLACK",fg="WHITE")
l2.grid(row=2,column=3)

l3=Label(screen,text="Adress",background="BLACK",fg="WHITE")
l3.grid(row=3,column=3)

l4=Label(screen,text="Email",background="BLACK",fg="WHITE")
l4.grid(row=4,column=3)

l5=Label(screen,text="Mobile",background="BLACK",fg="WHITE")
l5.grid(row=5,column=3)

l6=Label(screen,text="Birthday",background="BLACK",fg="WHITE")
l6.grid(row=6,column=3)

c2=Entry(screen,background="BLACK",fg="WHITE")
c2.grid(row=2,column=4,padx=5)

c3=Entry(screen,background="BLACK",fg="WHITE")
c3.grid(row=3,column=4,padx=5)

c4=Entry(screen,background="BLACK",fg="WHITE")
c4.grid(row=4,column=4,padx=5)

c5=Entry(screen,background="BLACK",fg="WHITE")
c5.grid(row=5,column=4,padx=5)

c6=Entry(screen,background="BLACK",fg="WHITE")
c6.grid(row=6,column=4,padx=5)

b2=Button(screen,text="Edit",background="BLACK",fg="WHITE")
b2.grid(row=7,column=0,padx=12,pady=12)

b3=Button(screen,text="Delete",background="BLACK",fg="WHITE")
b3.grid(row=7,column=1,pady=12)

b4=Button(screen,text="Update",background="BLACK",fg="WHITE")
b4.grid(row=7,column=4,pady=12)

b5=Button(screen,text="Save",background="BLACK",fg="WHITE")
b5.grid(row=8,column=1,pady=10,columnspan=3)

screen.mainloop()
