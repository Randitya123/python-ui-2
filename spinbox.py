from tkinter import*
s=Tk()
s.geometry("100x23")
s.config(background="black")
#creating spinbox
sb=Spinbox(s,from_=0,to=100)
sb.pack()
s.mainloop()