import tkinter 
import random

farba=['black','green', 'yellow', 'blue', 'brown']
farba_index = 0

def nahodny_kruh():
    global farba, farba_index
    x, y = random.randrange(640), random.randrange(480)
    c.create_oval(x-5, y-5, x+5, y+5, fill=farba[farba_index%len(farba)])
    c.after(1, nahodny_kruh)
def zmen_farba(event):
    global farba_index
    farba_index += 1
root = tkinter.Tk()
c = tkinter.Canvas(bg='red', width=640, height=480)
c.pack()
c.after(1, nahodny_kruh)
c.bind('<space>', zmen_farba)

c.focus_set()


root.mainloop()