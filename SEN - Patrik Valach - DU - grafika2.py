import tkinter
import random

root = tkinter.Tk()
WIDTH = 640
HEIGHT = 480
c = tkinter.Canvas(bg='white', width=WIDTH, height=HEIGHT)
c.pack()

def rand_oval(r, r_small, color):
    r = random.randint(r, min(WIDTH,HEIGHT)/2)
    
    x = random.randint(r,WIDTH-r)
    y = random.randint(r,HEIGHT-r)

    c.create_oval(x-r,y-r,  x+r,y+r, fill=color)

    for i in range(1000):
        xx = random.randint(r_small, WIDTH-r_small)
        yy = random.randint(r_small, HEIGHT-r_small)

        color_small = 'blue'
        if ((xx - x)**2  +  (yy - y)**2)**0.5 < r:
            color_small = 'red'

        c.create_oval(xx-r_small,yy-r_small,  xx+r_small,yy+r_small, fill=color_small)
rand_oval(100, 5, 'green')

root.mainloop()