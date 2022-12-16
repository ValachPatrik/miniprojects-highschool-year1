import tkinter 

def obdl(x0, y0, x1, y1):
    c.create_line(x0,y0, x1,y0, x1,y1, x0,y1, x0,y0)
    stredx, stredy = x0+(x1-x0)/2, y0+(y1-y0)/2,
    c.create_oval(stredx-5,stredy-5, stredx+5,stredy+5, fill='red')
root = tkinter.Tk()
c = tkinter.Canvas(width=640, height=480)
c.pack()

obdl(50, 60, 200, 300)

c.focus_set()


root.mainloop()