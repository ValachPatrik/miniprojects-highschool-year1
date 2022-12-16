import tkinter 
import random

farba = ['green', 'yellow', 'red']
farba_cislo = -1
def click(event):
    global x, y
    x,y = event.x, event.y
def move(event):
    global x, y, hrubka, farba, farba_cislo
    c.create_line(x,y,event.x,event.y, width=hrubka, fill=farba[farba_cislo%len(farba)], capstyle=tkinter.ROUND)
    click(event)
def release(event):
    global  hrubka, farba_cislo
    hrubka = random.randint(5,50)
    farba_cislo += 1
release(None)

root = tkinter.Tk()

c = tkinter.Canvas(width=640, height=480)
c.bind('<Button-1>', click)
c.bind('<B1-Motion>', move)
c.bind('<ButtonRelease-1>', release)
c.pack()
c.focus_set()

root.mainloop()