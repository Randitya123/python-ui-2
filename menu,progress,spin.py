from tkinter import*
from tkinter.ttk import*
from time import strftime
s=Tk()
s.title("Widget")
m1=Menu(s)
#adding file menu
f1=Menu(m1,tearoff=0)
m1.add_cascade(label="File",menu=f1)
f1.add_command(label="New Text File",command=None)
f1.add_command(label="New File",command=None)
f1.add_command(label="New Window",command=None)
#adding edit menu
f2=Menu(m1,tearoff=0)
m1.add_cascade(label="Edit",menu=f2)
f2.add_command(label="Undo",command=None)
f2.add_command(label="Redo",command=None)
f2.add_separator()
f2.add_command(label="Cut",command=None)
f3=Menu(m1,tearoff=0)
m1.add_cascade(label="View",menu=f3)
f3.add_command(label="Explorer",command=None)
f3.add_command(label="Search",command=None)
f3.add_command(label="Run",command=None)
f3.add_separator()
f3.add_command(label="Chat",command=None)
f3.add_command(label="Problems",command=None)
s.config(menu=m1)
#bar
p3=Progressbar(s,orient=HORIZONTAL,length=100,mode="determinate").place(x=100,y=100)
#function for the progress
def progbar():
    import time
    p3['value']=20
    s.update_idletasks()
    time.sleep(2)
    p3['value']=40
    s.update_idletasks()
    time.sleep(2)
    p3['value']=60
    s.update_idletasks()
    time.sleep(2)
    p3['value']=80
    s.update_idletasks()
    time.sleep(2)
    p3['value']=100
#button for progress
b1=Button(s,width=15,text="start",command=progbar).place(x=110,y=200)

s.mainloop()
