from tkinter import*
from tkinter.ttk import*

s=Tk()

e1var=StringVar()
e1=Entry(s,width=20,textvariable=e1var,font=("Arial",15))
e1.grid(row=0,column=0,columnspan=4,pady=10)
#button positon
l1=[
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("+",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("-",4,3)
]
#creating the buttons
for (text,row,column) in l1:
    if text=="=":
        b1=Button(s,width=5,text=text,command=s.destroy)
    else:
        b1=Button(s,width=5,text=text,)
    b1.grid(row=row,column=column,columnspan=4,pady=5)
s.mainloop()