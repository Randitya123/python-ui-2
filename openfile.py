from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import askopenfile
s=Tk()
s.geometry("220x180")
def openf():
    trig=askopenfile(mode="r",filetypes=[('Python File','*.py')])
    if trig is not None:
        readf=trig.read()
        print(readf)
b1=Button(s,width=10,text="open",command=openf).pack()
s.mainloop()