x = int(input('Zadaj rok: '))


if x % 4 == 0:
    odpoved = 'je priestupný (je deliteľný 4 a nie je 100)'
    if x % 100 == 0:
        odpoved = 'nie je priestupný (je deliteľný 4 aj 100, ale nie 400)'
        if x % 400 == 0 :
            odpoved = 'je priestupný (je deliteľný 4 aj 100 aj 400)'
else:
    odpoved = 'nie je priestupný (nie je deliteľný 4)'

print (x, odpoved)