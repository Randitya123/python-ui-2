from tkinter import*
from gtts import gTTS
import os
screen=Tk()
screen.geometry("300x360")
f1=Frame(screen,bg="red",height="150")
f1.pack(fill=X)
f2=Frame(screen,bg="green",height="220")
f2.pack(fill=X)
l1=Label(f1,text="Text to speech",font=("Cambria",15))
l1.place(x=80,y=100)
e1=Entry(f2,width=20,bd=3,font=10)
e1.place(x=50,y=100)
screen.mainloop()