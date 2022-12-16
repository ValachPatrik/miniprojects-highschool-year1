import random

n = int(input('Zadaj n: '))
s = int(input())
x = random.randint(0,n)
pokus = 0
while s != x:
    if x > s:
        print('Hadane cislo je vacsie')
    else:
        print ('Hadane cislo je mensie')
    pokus += 1
    s = int(input())
print('pocet pokusov', pokus)
