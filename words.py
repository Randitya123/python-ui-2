from tkinter import*
import tkinter
import random
from tkinter import messagebox
screen=Tk()
screen.geometry("350x200")
screen.config(background="lightblue")

l1=Label(screen,text="JUMBLED WORD GAME",bg="lightblue",font=("Cambria",15)).pack()
l2=Label(screen,text="gsdfgsdf",bg="lightblue",font=("Cambria",15)).pack()
c1=Entry(screen,background="BLACK",fg="WHITE").pack()
b1=Button(screen,text="Check",background="White",fg="Green").pack()
b2=Button(screen,text="Reset",background="White",fg="Yellow").pack()
l3=Label(screen,text="Score:",bg="lightblue",font=("Cambria",15)).pack()



screen.mainloop()
