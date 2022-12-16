def cislo(s):
    for i in s:
        if '0' > i or i > '9':
            return False
    return True

def velke(s):
    a = 0
    for i in s:
        if 'A' <= i <= 'Z':
            a += 1
    return a

def binary(n, x, y):
    h = ''
    while (n > 0):
        i = n % 2
        if i == 1:
            h = y + h
        else:
            h = x + h
        n //= 2
    return h

s = str(input('Zadaj string pre funkciu cislo: '))
print(cislo(s))

t = str(input('Zadaj string pre funkciu velke: '))
print(velke(t))

n = int(input('Zadaj n: '))
a = str(input('Prvy charakter: '))
b = str(input('Druhy charakter: '))
print(binary(n, a, b))