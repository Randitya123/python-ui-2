from tkinter import*
s=Tk ()
s.geometry("800x600")
s.config(background="pink") 
l1=Label(s,background="pink",text="Username",font=("cambria",40)).place(x=50, y=50)
l2=Label(s,background="pink",text="Password",font=("cambria",40)).place(x=50, y=150)
c1=Entry(s,bg="white",fg="black",width=15,font=("cambria",40)).place(x=300, y=50)
c2=Entry(s,bg="white",fg="black",width=15,font=("cambria",40)).place(x=300, y=150)
s.mainloop()