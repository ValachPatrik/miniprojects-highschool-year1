import tkinter 
import random

color = ['green', 'yellow', 'red']
i = 0
xy = []
xy1 = []
stvorec = None
def click(event):
    global i
    d = random.randint(5,51)
    c.create_oval(event.x-d/2, event.y-d/2, event.x+d/2, event.y+d/2, fill=color[i%3])
    i += 1

def ciara(event):
    global xy
    xy += [event.x, event.y]
    if len(xy) == 4:
        c.create_line(xy)
        xy = []
def zrus(event):
    global xy
    xy = []

def stvorec1(event):
    global xy1
    xy1 += [event.x, event.y]
    if len(xy1) == 4:
        c.create_rectangle(xy1)
        xy1 = []
def stvorec2(event):
    global stvorec
    if stvorec:
        c.delete(stvorec)
    if xy1:
        stvorec = c.create_rectangle(xy1, event.x, event.y)
        
def pismenko(event):
    X1 = random.randint(5,635)
    Y1 = random.randint(5,475)
    c.create_text(X1, Y1, text=event.char)
root = tkinter.Tk()

c = tkinter.Canvas(bg='red', width=640, height=480)
#c.bind('<Button-1>', click)

#c.bind('<Button-1>', ciara)
#c.bind('<Button-3>', zrus)

#c.bind('<Button-1>', stvorec1)
#c.bind('<Motion>', stvorec2)

#c.bind('<Key>', pismenko)
c.pack()
c.focus_set()

root.mainloop()