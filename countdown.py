from tkinter import*
from tkinter import messagebox
import time
screen=Tk()
screen.geometry("100x100")

h=StringVar()
m=StringVar()
s=StringVar()
h.set("00")
m.set("00")
s.set("00")
e1=Entry(screen,width=3,textvariable=h,font=4)
e1.place(x=5,y=20)
e2=Entry(screen,width=3,textvariable=m,font=4)
e2.place(x=45,y=20)
e3=Entry(screen,width=3,textvariable=s,font=4)
e3.place(x=85,y=20)
def times():
    try:
        temptime=int(h.get())*3600+int(m.get())*60+int(s.get())*1
    except:
        print("Wrong")
    while temptime>-1:
        #coversion of total time into minutes and seconds
        min,secs=divmod(temptime,60)
        hour=0
        if min>60:
            #coversion of total time into hour and minutes
            hour,min=divmod(min,60)
        h.set("{00:2d}".format(hour))
        m.set("{00:2d}".format(min))
        s.set("{00:2d}".format(secs))
        screen.update()
        time.sleep(1)
        if temptime==0:
            messagebox.showinfo("countdown","Time is up!")
        temptime-=1
b1=Button(screen,text="set time countdown",width=15,background="gold",command=times)
b1.place(x=2,y=60)
screen.mainloop()
