from tkinter import*
s=Tk()
s.geometry("500x500")
#function for conversion
def convert():
   c=float(cels.get())*33.8
   t1.delete("1.0",END)
   t1.insert(END,c)
l1=Label(s,text="Enter the temperature in celius:",font=("cambria",16),foreground="black").place(x=0,y=20)
cels=StringVar()
c1=Entry(s,textvariable=cels,width=10,background="white",font=("cambria",25),foreground="black").place(x=300,y=20)
b1=Button(s,text="Convert",command=convert,background="grey").place(x=200,y=80)
l2=Label(s,text="GRAM",font=("cambria",16),foreground="black")
l1=Label(s,text="Temperature in fahrenheit:",font=("cambria",16),foreground="black").place(x=0,y=300)
t1=Text(s,height=2,width=20)
t1.place(x=300,y=300)


s.mainloop()
