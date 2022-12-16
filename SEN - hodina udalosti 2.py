import tkinter 
import time 
import random

cas = 10
objekt_cas = None
text_odpocet = None
x, y = 320, 240
objekt_kruh = None
farba=['black','green', 'yellow', 'blue', 'brown']
farba_index = 0
def sekunda(): #1
    global cas, text_odpocet
    c.delete(text_odpocet)
    text_odpocet = c.create_text(320, 240, text=cas)
    cas -= 1
    if cas >= 0:
        c.after(1000, sekunda)
def real_time(): #2
    global objekt_cas
    c.delete(objekt_cas)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    objekt_cas = c.create_text(300, 200, text=current_time)
    c.after(1000, real_time)
def kruh(event): #3
    global objekt_kruh, x, y
    if event.char == 'w':
        y -= 5
    elif event.char == 'a':
        x -= 5
    elif event.char == 's':
        y += 5
    elif event.char == 'd':
        x += 5
    c.delete(objekt_kruh)
    objekt_kruh = c.create_oval(x-10,y-10,x+10,y+10, fill='green')
def nahodny_kruh(): #DU
    global farba, farba_index
    x, y = random.randrange(640), random.randrange(480)
    c.create_oval(x-5, y-5, x+5, y+5, fill=farba[farba_index%len(farba)])
    c.after(1000, nahodny_kruh)
def zmen_farba(event):
    global farba_index
    farba_index += 1
root = tkinter.Tk()

c = tkinter.Canvas(bg='red', width=640, height=480)
c.pack()
#1
c.after(1000, sekunda)
#2
c.after(1000, real_time)
#3
objekt_kruh = c.create_oval(x-10,y-10,x+10,y+10, fill='green')
c.bind('<Key>', kruh)
# DU
c.after(1000, nahodny_kruh)
c.bind('<space>', zmen_farba)

c.focus_set()


root.mainloop()