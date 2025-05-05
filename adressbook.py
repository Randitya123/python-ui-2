from tkinter import*
from tkinter.filedialog import*
from tkinter import messagebox
#4from tkinter.ttk import*
screen=Tk()
#function 
Adress={}
def clear():
    c2.delete(0,END)
    c3.delete(0,END)
    c4.delete(0,END)
    c5.delete(0,END)
    c6.delete(0,END)
#add or update
def add():
    key=c2.get()
    if key=="":
        messagebox.showinfo("ERROR 504","Name could not be found")
    else:
        if key not in Adress.keys():
            list1.insert(END, key)
        #update
        Adress[key]=(c3.get(),c4.get(),c5.get(),c6.get())
        clear()

#def edit():
def display(event):
    window=Toplevel(screen)
    index=list1.curselection()
    contact=""
    if index==True:
        key=list1.get(index)
        contact="NAME:+key"+"\n\n"
        details=Adress[key]
        contact+="ADDRESS:"+details[0]+"\n"
        contact+="EMAIL:"+details[1]+"\n"
        contact+="MOBILE:"+details[2]+"\n"
        contact+="BRITHDAY:"+details[3]+"\n"
    label=Label(window)
    label.grid(row=0,column=0)
    label.configure(text=contact)
#widgets
screen.configure(bg="black")
l1=Label(screen,text="My Adress Book",width=25)
l1.grid(row=0,column=0,pady=10, columnspan=3)

b1=Button(screen,text="OPEN",background="BLACK",fg="WHITE")
b1.grid(row=0,column=4,pady=10)

list1=Listbox(screen,height=15,width=30)
list1.grid(row=2,column=0,columnspan=3,rowspan=5)
list1.bind("<<ListboxSelect>>",display)

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

b4=Button(screen,text="Update/Add",background="BLACK",fg="WHITE",command=add)
b4.grid(row=7,column=4,pady=12)

b5=Button(screen,text="Save",background="BLACK",fg="WHITE")
b5.grid(row=8,column=1,pady=10,columnspan=3)

screen.mainloop()
