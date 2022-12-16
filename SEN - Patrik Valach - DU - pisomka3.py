import tkinter 

def pyramida(event):
    x0, y0 = 50, 450
    r = 20
    c.delete('all')
    if '1' <= event.char <= '9':
        for i in range(int(event.char)+1):
            for j in range(i):
                c.create_oval(x0+j*2*r, y0-i*2*r, x0+(j+1)*2*r, y0-(i+1)*2*r, fill='red')

root = tkinter.Tk()
c = tkinter.Canvas(width=640, height=480)
c.pack()

c.bind('<Key>', pyramida)

c.focus_set()


root.mainloop()