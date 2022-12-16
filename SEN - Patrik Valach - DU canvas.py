import tkinter
import random

root = tkinter.Tk()

c = tkinter.Canvas(width=700, height=500)
c.pack()

list_xy = []
farby = ['yellow', 'red', 'green']

for i in range(9):
    x = random.randint(0,600)
    y = random.randint(0,400)

    c.create_oval(x,y,  x+100,y+100, width=3, outline='black', fill=farby[i%3])

    list_xy.append(x+50)
    list_xy.append(y+50)

c.create_line(list_xy, fill='dark blue', width=10)

root.mainloop()