from tkinter import*
from tkinter.ttk import*
s=Tk()
s.config(background="black")
s.geometry("400x800")
s.title("Mathmetical Table")
def command1():
    tables=""
    for i in range(r1.get()+1):
        tables+=str(d1.get())+" * "+str(i)+" = "+str(d1.get()*i)+"\n"
    l3.configure(text=tables)
l1=Label(s,text="Number and range:",font=("arial",10),background="black",foreground="white").place(x=20,y=100)
l2=Label(s,text="Mathmetical Table",font=("arial",10),background="black",foreground="white").place(x=160,y=20)
l3=Label(s,font=("arial",12),background="black",foreground="white",anchor="center")
l3.place(x=155,y=220)
d1=IntVar()
dropdown=Combobox(s,textvariable=d1,width=7)
#adding values to the dropdown
dropdown['values']=tuple(range(101))
dropdown.place(x=170,y=100)
r1=IntVar()
radio1=Radiobutton(s,text="10",variable=r1,value=10)
radio1.place(x=350,y=100)
radio2=Radiobutton(s,text="20",variable=r1,value=20)
radio2.place(x=350,y=135)
radio3=Radiobutton(s,text="30",variable=r1,value=30)
radio3.place(x=350,y=170)
r1.set(10)
b1=Button(s,command=command1,text="Generate")
b1.place(x=165,y=170)
s.mainloop()
