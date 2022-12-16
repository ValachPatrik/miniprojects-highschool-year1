n = int(input('Zadaj n: '))

for i in range (3, n):
    prvocislo_check = True
    for j in range (2, i):
        if i % j == 0:
            prvocislo_check = False
    for j in range (2, i):
        if (i+2) % j == 0 or (i+2) >= n:
            #termin 'ostro' mensie som nikde nenasiel ci znamena < alebo <=, v tomto if-e a hore v range to viem jednoducho zmenit keby bolo treba
            prvocislo_check = False
    if prvocislo_check == True:
        print (i, i+2)