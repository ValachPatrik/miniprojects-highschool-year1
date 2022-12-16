import tkinter
import random

sirka = []
vyska = []
x = []
y = []
def rrectangle():
    global sirka, vyska, x, y
    sirka += [random.randint(0, WIDTH)]
    vyska += [random.randint(0, HEIGHT)]
    x += [random.randint(0, WIDTH - sirka[-1])]
    y += [random.randint(0, HEIGHT - vyska[-1])]
    c.create_rectangle(x[-1],y[-1],x[-1]+sirka[-1],y[-1]+vyska[-1], fill="green")
def click(event):
    r = 5
    farba = 'blue'
    if (event.x > x[0] and event.x < x[0]+sirka[0] and event.y > y[0] and event.y < y[0]+vyska[0]) or (event.x > x[1] and event.x < x[1]+sirka[1] and event.y > y[1] and event.y < y[1]+vyska[1]):
        farba = 'red'
        if (event.x > x[0] and event.x < x[0]+sirka[0] and event.y > y[0] and event.y < y[0]+vyska[0]) and (event.x > x[1] and event.x < x[1]+sirka[1] and event.y > y[1] and event.y < y[1]+vyska[1]):
            farba = 'yellow'
    c.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill=farba)


root = tkinter.Tk()

WIDTH = 640
HEIGHT = 480
c = tkinter.Canvas(width=WIDTH, height=HEIGHT)

for i in range(2):
    rrectangle()
c.bind('<Button-1>', click)

c.pack()
c.focus_set()

root.mainloop()