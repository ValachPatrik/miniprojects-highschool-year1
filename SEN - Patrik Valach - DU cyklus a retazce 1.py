cislo = str(int(input ('Zadaj cislo: ')))
sucin = 1
i=0
while i != len(cislo):
    sucin = sucin * int(cislo[i])
    i += 1
print (int(sucin + len(cislo)))