import tkinter 

x0,y0,x1,y1 = 20,50,200,300

root = tkinter.Tk()
def ciara(x0,y0,x1,y1):
    x = (x1-x0)/100
    y = (y1-y0)/100
    for i in range(100):
        c.create_oval(x0+x*i-10, y0+y*i-10, x0+x*i+10, y0+y*i+10)
c = tkinter.Canvas(width=640, height=480)
c.pack()
ciara(x0,y0,x1,y1)
c.focus_set()


root.mainloop()