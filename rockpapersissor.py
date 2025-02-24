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
    startgame.config(text="Its a tie!")
    myscore.config(text="Your score:"+str(p1score))
    computerscore.config(text="Computers score:"+str(compscore))
def compwin():
    global p1score, compscore
    startgame.config(text="Computer Won!")
    compscore+=1
    myscore.config(text="Your score:"+str(p1score))
    computerscore.config(text="Computers score:"+str(compscore))
def p1win():
    global p1score, compscore
    startgame.config(text="You Won!")
    p1score+=1
    myscore.config(text="Your score:"+str(p1score))
    computerscore.config(text="Computers score:"+str(compscore))
def p1choice(p1input):
    global p1score, compscore
    print(p1input)
    computerchoiceyes=computerchoice()
    userselection.config(text="Your selection:"+p1input[0])
    computerselection.config(text="Computers selection:"+computerchoiceyes[0])
    if p1input==computerchoiceyes:
        tie()
    #player chooses rock
    if p1input[1]==0:
        if computerchoiceyes[1]==1:
            compwin()
        if computerchoiceyes[1]==2:
            p1win()
    if p1input[1]==1:
        if computerchoiceyes[1]==0:
            p1win()
        if computerchoiceyes[1]==2:
            compwin()
    if p1input[1]==2:
        if computerchoiceyes[1]==0:
            compwin()
        if computerchoiceyes[1]==1:
            p1win()
l1=Label(s,text="Rock Paper Scissor",font=("arial",15,"bold"),background="lightgrey",foreground="black").place(x=170,y=0)
l2=Label(s,text="Your Option:",font=("arial",10,"bold"),background="lightgrey",foreground="black").place(x=30,y=70)
l3=Label(s,text="Your Score:",font=("arial",10,"bold"),background="lightgrey",foreground="black").place(x=30,y=170)
#complicated labels
userselection=Label(s,text="Your selection:---",font=("arial",10),background="lightgrey",foreground="black")
userselection.place(x=30,y=210)
computerselection=Label(s,text="Computers selection:---",font=("arial",10),background="lightgrey",foreground="black")
computerselection.place(x=30,y=260)
myscore=Label(s,text="Your score:-",font=("arial",10),background="lightgrey",foreground="black")
myscore.place(x=300,y=210)
computerscore=Label(s,text="Computers score:-",font=("arial",10),background="lightgrey",foreground="black")
computerscore.place(x=300,y=260)
startgame=Label(s,text="Lets start the game",font=("arial",12),background="lightgrey",foreground="yellow")
startgame.place(x=195,y=25)

b1=Button(s,width=18,text="Rock",fg="lightgrey",background="Red",command=lambda:p1choice(list1[0])).place(x=30,y=110)
b2=Button(s,width=18,text="Paper",fg="lightgrey",background="blue",command=lambda:p1choice(list1[1])).place(x=183,y=110)
b3=Button(s,width=18,text="Scissor",fg="lightgrey",background="green",command=lambda:p1choice(list1[2])).place(x=340,y=110)
s.mainloop()
