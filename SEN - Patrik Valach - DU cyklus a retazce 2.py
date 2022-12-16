n = int(input('Zadaj cislo: '))
pocet_medzier = n
for i in range (1,n+1):
    pocet_medzier -= 1
    print (pocet_medzier*' ' + i*'*')