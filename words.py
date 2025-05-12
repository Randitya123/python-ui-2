from tkinter import*
import tkinter
import random
from tkinter import messagebox
screen=Tk()
screen.geometry("350x200")
screen.config(background="lightblue")
#list for words and answers
index1=0
index2=0
list1 = [
    "Abandon", "Benefit", "Cautious", "Decent", "Eager",
    "Familiar", "Genuine", "Hesitate", "Ignore", "Justice",
    "Knowledge", "Loyal", "Manage", "Noticeable", "Occur",
    "Predict", "Reasonable", "Scarce", "Tidy", "Unusual",
    "Visible", "Warn", "Yield", "Zeal", "Balance"
]
jumbled_list = [
    "ndAbona", "tnBefei", "tsuCuoai", "enctDe", "rEega",
    "alFriami", "eGiunnee", "taseHie", "erogIn", "tsucJie",
    "Kwelndgoe", "Lyoal", "gMnaae", "acNleotibe", "cOcru",
    "tdPeicr", "oeRsabneal", "screSa", "dTiy", "slaUuun",
    "blseVii", "nWra", "dYile", "aleZ", "nBcalea"
]
num=random.randrange(0,len(jumbled_list))
dt=""
#functions
def reset():
    global list1,jumbled_list
    num=random.randrange(0,len(jumbled_list))
    l2.config(text=jumbled_list[num])
    c1.delete(0,END)
def check():
    global list1,jumbled_list, index1,index2,l3,dt,num
    index2=int(index2)+1
    useranswer=c1.get()
    if useranswer==list1[num]:
        messagebox.showinfo("ANSWER","You got it!")
        index1=int(index1)+1
    else:
        messagebox.showinfo("ANSWER","You got it wrong")
    dt='Score:'+str(index1)+'/'+str(index2)
    l3.forget()
    l3=Label(screen,text=dt)
    l3.pack(side=LEFT)
    reset()
def default():
    global list1,jumbled_list,num
    l2.config(text=jumbled_list[num])


l1=Label(screen,text="JUMBLED WORD GAME",bg="lightblue",font=("Cambria",15))
l1.pack()
l2=Label(screen,text="",bg="lightblue",font=("Cambria",15))
l2.pack()
c1=Entry(screen,background="BLACK",fg="WHITE",width=17)
c1.pack()
b1=Button(screen,text="Check",background="White",fg="Green",command=check)
b1.pack(padx=10,pady=10)
b2=Button(screen,text="Reset",background="White",fg="Black",command=reset)
b2.pack()
l3=Label(screen,text="Score:",bg="lightblue",font=("Cambria",15))
l3.pack()
default()


screen.mainloop()
