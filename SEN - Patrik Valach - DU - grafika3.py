import tkinter

root = tkinter.Tk()
WIDTH = 640
HEIGHT = 480
c = tkinter.Canvas(bg='white', width=WIDTH, height=HEIGHT)
c.pack()

def zebra (x,y):
    d = 50
    obdlz_pocet = 6
    obdlz_sirka, obdlz_vyska = 40, 120
    posun_hlavy = 20
    chvost_sirka, chvost_dlzka = 5, 80
    farby = ['white', 'black']

    c.create_oval(x,y, x+d,y+d, fill=farby[1])
    for i in range(obdlz_pocet):
        c.create_rectangle(x+d+i*obdlz_sirka, y+posun_hlavy,  x+d+(i+1)*obdlz_sirka, y+posun_hlavy+obdlz_vyska, fill=(farby[i%len(farby)]))
    c.create_line(x+d+(i+1)*obdlz_sirka, y+posun_hlavy,  x+d+(i+2)*obdlz_sirka, y+posun_hlavy+chvost_dlzka, width=chvost_sirka, fill=farby[1])

zebra(50,20)
root.mainloop()