from tkinter import*
screen=Tk()

f1=Frame(screen,bg="red")
b1=Button(screen,text="OPEN",background="BLACK",fg="WHITE")
b2=Button(screen,text="ADD",background="BLACK",fg="WHITE")
b3=Button(screen,text="DELETE",background="BLACK",fg="WHITE")
b4=Button(screen,text="SAVE",background="BLACK",fg="WHITE")
c1=Entry(screen,width=10,background="BLACK",font=("arial",10),foreground="WHITE")
#packing itmee[sx]edpnvfklnfvol;'sfvmd
b1.pack(side=LEFT,padx=5,pady=5)
b3.pack(side=RIGHT,padx=5,pady=5)
b4.pack(padx=5,pady=5)
c1.pack(padx=5,pady=5)
b2.pack(padx=5,pady=5)
scroll=Scrollbar(f1,orient="vertical")
scroll.pack(side=RIGHT,fill=Y)
list1=Listbox(f1,width=80,yscrollcommand=scroll.set,bg="red")
for dt in range(100001):
    list1.insert(END,"LIST"+ str(dt))
list1.pack(side=LEFT,padx=5,pady=5)
scroll.config(command=list1.yview)
f1.pack(side=RIGHT)
screen.mainloop()