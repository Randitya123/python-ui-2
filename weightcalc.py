from tkinter import*
s=Tk()
#function for conversion
def convert():
   g=float(kgs.get())*1000
   p=float(kgs.get())*2.20462
   o=float(kgs.get())*35.274
   t1.delete("1.0",END)
   t1.insert(END,g)
   t2.delete("1.0",END)
   t2.insert(END,p)
   t3.delete("1.0",END)
   t3.insert(END,o)
l1=Label(s,text="Enter the weight in KG",font=("cambria",16),foreground="black")
kgs=StringVar()
c1=Entry(s,textvariable=kgs,width=10,background="white",font=("cambria",25),foreground="black")
b1=Button(s,text="Convert",command=convert,background="grey")
l2=Label(s,text="GRAM",font=("cambria",16),foreground="black")
l3=Label(s,text="POUNDS",font=("cambria",16),foreground="black")
l4=Label(s,text="OUNCE",font=("cambria",16),foreground="black")
t1=Text(s,height=2,width=10)
t2=Text(s,height=2,width=10)
t3=Text(s,height=2,width=10)
l1.grid(row=0,column=0)
c1.grid(row=0,column=1)
b1.grid(row=0,column=2)
l2.grid(row=1,column=0)
l3.grid(row=1,column=1)
l4.grid(row=1,column=2)
t1.grid(row=2,column=0)
t2.grid(row=2,column=1)
t3.grid(row=2,column=2)
s.mainloop()
