    import tkinter 

xy=[]
def oval(event):
    global xy
    xy += [event.x, event.y]
    if len(xy) == 4:
        c.create_oval(xy)
        xy = []

root = tkinter.Tk()
c = tkinter.Canvas(width=640, height=480)
c.pack()

c.bind('<Button-1>', oval)

c.focus_set()


root.mainloop()