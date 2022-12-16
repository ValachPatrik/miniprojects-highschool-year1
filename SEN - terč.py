import tkinter

root = tkinter.Tk()

c = tkinter.Canvas(width=700, height=500)
c.pack()

farba = ['red','green', 'blue']
for i in range (10):
    
    c.create_oval(10+i*10,10+i*10, 250-i*10,250-i*10, fill=farba[i%3])

root.mainloop()