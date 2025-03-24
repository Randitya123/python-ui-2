from tkinter import*
screen=Tk()
screen.geometry("400x400")
screen.config(background="black")

def calcdistance():
    try:
        times=float(c1.get())
        speeds=float(c2.get())
        distances=times*speeds
        l4.config(text=f"Distance Covered: {distances:.2f} unit")
    except ValueError:
        l4.config(text="Wrong input")
b1=Button(screen,text="Calculate Distance",background="Red",command=calcdistance)
b1.place(x=150,y=320)
l1=Label(screen,text="Distance Calculator",font=("arial",15),background="black",foreground="Red")
l1.place(x=120,y=50)
l2=Label(screen,text="Enter Time(Hour):",font=("arial",12),background="black",foreground="white")
l2.place(x=130,y=130)
l3=Label(screen,text="Enter Speed(unit or hr):",font=("arial",12),background="black",foreground="white")
l3.place(x=130,y=220)
l4=Label(screen,text="",font=("arial",12),background="black",foreground="white")
l4.place(x=15,y=350)
c1=Entry(screen,width=15,background="white",font=("cambria",10),foreground="Black")
c1.place(x=130,y=170)
c2=Entry(screen,width=15,background="white",font=("cambria",10),foreground="Black")
c2.place(x=130,y=260)


screen.mainloop()