from tkinter import*
s=Tk()
s.geometry("500x500")
s.config(background="red")
b1=Button(s,width=20,text="Submit order",fg="white",background="blue",command=s.destroy).place(x=180,y=450)
l1=Label(s,text="Email",font=("arial",10),background="WHITE",foreground="black").place(x=100,y=50)
l2=Label(s,text="Password",font=("arial",10),background="WHITE",foreground="black").place(x=100,y=100)
l3=Label(s,width=45,text="Which food will you like?",font=("arial",10),background="WHITE",foreground="black").place(x=100,y=150)
l4=Label(s,width=45,text="Which dessert will you like?",font=("arial",10),background="WHITE",foreground="black").place(x=100,y=250)
l5=Label(s,width=45,text="Which beverage will you like?",font=("arial",10),background="WHITE",foreground="black").place(x=100,y=350)
c1=Entry(s,width=40,background="grey",font=("arial",10),foreground="black").place(x=185,y=50)
c2=Entry(s,width=40,background="grey",font=("arial",10),foreground="black").place(x=185,y=100)
c3=Entry(s,width=20,background="grey",font=("arial",10),foreground="black").place(x=100,y=190)
c4=Entry(s,width=20,background="grey",font=("arial",10),foreground="black").place(x=100,y=290)
c5=Entry(s,width=20,background="grey",font=("arial",10),foreground="black").place(x=100,y=390)
sb=Spinbox(s,from_=0,to=5).place(x=320,y=190)
sb1=Spinbox(s,from_=0,to=5).place(x=320,y=290)
sb2=Spinbox(s,from_=0,to=5).place(x=320,y=390)
s.mainloop()
