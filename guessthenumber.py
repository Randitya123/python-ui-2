from tkinter import*
from tkinter import messagebox
import random
s=Tk()
s.geometry("200x200")
def randomnumber():
    random1=random.randint(1,10)
    random2=random.randint(1,10)
    return random1,random2,random1*random2
num1,num2,ans=randomnumber()
#check func
def check():
    try:
        guess=int(c1.get())
        if ans==guess:
            messagebox.showinfo("Good","Good job")
        else:
            messagebox.showerror("error","absolutely wrong")
    except ValueError:
        messagebox.showerror("error","invalid input")
def generate():
    global num1, num2, ans
    num1,num2,ans=randomnumber()
    messagebox.showinfo("Guess number","one of the random number is:{}".format(num1))
    c1.delete(0, END)
l1=Label(s,text="Guess the product of {} and ?".format(num2),font=("arial",10),background="WHITE",foreground="black")
l1.place(x=20,y=0)
c1=Entry(s,width=20,background="grey",font=("arial",10),foreground="black")
c1.place(x=20,y=50)
b1=Button(s,width=5,text="Check",fg="white",background="blue",command=check)
b1.place(x=20,y=100)
b2=Button(s,width=7,text="New Game",fg="white",background="blue",command=generate)
b2.place(x=20,y=140)
generate()
s.mainloop()
