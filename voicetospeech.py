from tkinter import*
import speech_recognition as sr
from tkinter import messagebox
from tkinter import filedialog

screen=Tk()
screen.geometry("500x500")
def translate():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print("microphone started recording")
        audio=rec.listen(source)
        try:
            text=rec.recognize_google(audio)
        except:
            text="sorry couldnt recognize your voice" 
        t1.delete(1.0,END)
        t1.insert(END,text)

def save():
    filedia=filedialog.asksaveasfile(defaultextension=".txt")
    if filedia:
        filedia.write(t1.get (1.0, END))
        filedia.close()
    else:
        messagebox.info("warning","text error")

l1=Label(screen,text="Speech to text",foreground="black",font=("Cambria",25))
l1.place(x=170,y=15)
t1=Text(screen,height=4,width=30,bd=3,font=10)
t1.place(x=130,y=205)
b1=Button(screen,width=38,text="Click on me, \n to start recording",fg="white",background="blue",command=translate)
b1.place(x=130,y=130)
b2=Button(screen,width=38,text="Save File",fg="white",background="blue",command=save)
b2.place(x=130,y=320)

screen.mainloop()
