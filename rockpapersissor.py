from tkinter import*
import random
import tkinter.font as ft
s=Tk()
s.geometry("500x300")
s.config(bg="lightgrey")
#list for selection
list1=[('rock',0),('paper',1),('scissor',2)]
p1score=0
compscore=0
#getting computer choice
def computerchoice():
    return random.choice(list1)
def tie():
    global p1score, compscore
    startgame.config(Text="Its a tie!")
    myscore.congfig(Text="Your score:"+str(p1score))
    computerscore.congfig(Text="Computers score:"+str(compscore))
def compwin():
    global p1score, compscore
    startgame.config(Text="Computer Won!")
    compscore+=1
    myscore.congfig(Text="Your score:"+str(p1score))
    computerscore.congfig(Text="Computers score:"+str(compscore))
def p1win():
    global p1score, compscore
    startgame.config(Text="You Won!")
    p1score+=1
    myscore.congfig(Text="Your score:"+str(p1score))
    computerscore.congfig(Text="Computers score:"+str(compscore))
def p1choice(p1input):
    global p1score, compscore
    print(p1input)
l1=Label(s,text="Rock Paper Scissor",font=("arial",15,"bold"),background="lightgrey",foreground="black").place(x=170,y=0)
l2=Label(s,text="Your Option:",font=("arial",10,"bold"),background="lightgrey",foreground="black").place(x=30,y=70)
l3=Label(s,text="Your Score:",font=("arial",10,"bold"),background="lightgrey",foreground="black").place(x=30,y=170)
#complicated labels
userselection=Label(s,text="Your selection:---",font=("arial",10),background="lightgrey",foreground="black").place(x=30,y=210)
computerselection=Label(s,text="Computers selection:---",font=("arial",10),background="lightgrey",foreground="black").place(x=30,y=260)
myscore=Label(s,text="Your score:-",font=("arial",10),background="lightgrey",foreground="black").place(x=300,y=210)
computerscore=Label(s,text="Computers score:-",font=("arial",10),background="lightgrey",foreground="black").place(x=300,y=260)
startgame=Label(s,text="Lets start the game",font=("arial",12),background="lightgrey",foreground="yellow").place(x=195,y=25)


b1=Button(s,width=18,text="Rock",fg="lightgrey",background="Red").place(x=30,y=110)
b2=Button(s,width=18,text="Paper",fg="lightgrey",background="blue").place(x=183,y=110)
b3=Button(s,width=18,text="Scissor",fg="lightgrey",background="green").place(x=340,y=110)
s.mainloop()