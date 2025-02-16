from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import asksaveasfile
s=Tk()
s.geometry("200x150")
def save():
    filetype=[('All Files','*.*'),('Python Files','*.py'),('Text Document','*.txt')]
    trig=asksaveasfile(filetypes=filetype,defaultextension=filetype)
b1=Button(s,width=10,text="save",command=save).pack()
s.mainloop()