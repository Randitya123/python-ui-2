from tkinter import*
from tkinter.colorchooser import askcolor

class drawing(object):
    pensize=5.0
    defaultcol="black"
    def __init__(self):
        self.s=Tk()
        self.pen=Button(self.s,text="pen",font=("cambria",15),command=self.penn)
        self.pen.grid(row=0,column=0)
        self.brush=Button(self.s,text="brush",font=("cambria",15),command=self.paint)
        self.brush.grid(row=0,column=1)
        self.colors=Button(self.s,text="color",font=("cambria",15),command=self.colour)
        self.colors.grid(row=0,column=2)
        self.eraser=Button(self.s,text="eraser",font=("cambria",15),command=self.rubber)
        self.eraser.grid(row=0,column=3)
        self.pthick=Scale(self.s,from_=1,to=10,orient=HORIZONTAL)
        self.pthick.grid(row=0,column=4)
        self.screen=Canvas(self.s,bg="white",width=600,height=600)
        self.screen.grid(row=1,columnspan=5)
        self.everthing()
    # self.setup()
        self.s.mainloop()
    def penn(self):
        self.activate(self.pen)
        self.tool="pen"
    def activate(self,cbutton,eraser_mode=False):
        self.activebutton.config(relief=RAISED)
        cbutton.config(relief=SUNKEN)
        self.activebutton=cbutton
        self.eraser_on=eraser_mode
    def everthing(self):
        self.x=None
        self.y=None
        self.thickness=self.pthick.get(  )
        self.color=self.defaultcol
        self.eraser_on=False
        self.activebutton=self.pen
        self.tool="pen"
        self.screen.bind('<B1-Motion>', self.paint )
    def paint(self,event):
        self.thickness=self.pthick.get(  )
        paintcolor="white" if self.eraser_on else self.color
        if self.tool=="pen":
            if self.x and self.y:
                self.screen.create_line(self.x,self.y,event.x,event.y,width=self.thickness,fill=paintcolor,capstyle=ROUND,smooth=TRUE,splinesteps=36)
        elif self.tool=="brush":
            brushsize=self.thickness
            self.screen.create_oval(event.x-brushsize/2,event.y-brushsize/2,event.x+brushsize/2,event.y+brushsize/2,fill=paintcolor,outline=paintcolor)

        self.x=event.x
        self.y=event.y
    def colour(self):
        self.eraser_on=False
        self.color=askcolor(color=self.color)[1]
    def rubber(self):
        self.activate(self.eraser,eraser_mode=True)
        self.tool="eraser"
if __name__=='__main__':
    drawing()
