from tkinter import*
from gtts import gTTS
import os
screen=Tk()
screen.geometry("300x360")
f1=Frame(screen,bg="Black",height="150")
f1.pack(fill=X)
f2=Frame(screen,bg="Purple",height="220")
f2.pack(fill=X)
l1=Label(f1,text="Text to speech",background="black",foreground="white",font=("Cambria",15))
l1.place(x=80,y=70)
e1=Entry(f2,width=20,bd=3,font=10)
e1.place(x=50,y=80)
def textvoice():
    language="en"
    obj1=gTTS(text=e1.get(),lang=language,slow=False)
    obj1.save("voice.wav")
    os.system("voice.wav")
b1=Button(f2,width=5,text="Submit",fg="White",background="black",command=textvoice)
b1.place(x=120,y=150)

screen.mainloop()
