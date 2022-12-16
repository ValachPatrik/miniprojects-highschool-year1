import time

def vypis(n,s):
    samohlasky = 'aeiouAEIOU'
    samohlasky_pocet = 0

    for i in samohlasky:
        samohlasky_pocet += s.count(i)

    rychlost_vypisu = n / ((len(s)-samohlasky_pocet) *2 + samohlasky_pocet)
    for i in s:
        if i in samohlasky:
            time.sleep(rychlost_vypisu)
        else:
            time.sleep(rychlost_vypisu * 2)
        print(i,end='')

n = int(input('Zadaj n: '))
s = input('Zadaj strign: ')

vypis(n,s)