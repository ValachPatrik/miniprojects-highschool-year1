def generate_square(n):
    l = [1]
    x = 1
    while n >= (c := l[-1] + (x := x + 2)):
        l.append(c)
    return l

def parne (a):
    b = []
    for i in a:
        b.append(i)
        if i % 2 == 0:
            b.append(0)
    return b

def najcastejsie(a):
    naj = 0
    n = ''
    for i in a:
        pocet = a.count(i)
        if pocet > naj:
            naj = pocet
            n = i
    return n


n = int(input('Zadaj n: '))
print(generate_square(n))

a = [0, 1, 2, 3, 2, 2, 5]
print(parne(a))

a = [0, 1, 2, 3, 2, 2, 5]
print(najcastejsie(a))


#so Samuleom Doupilom sme sa nudili a skusali ako by sa dala jednotka urobit najefektivnejsie
#prva verzia sa ukazala ako najlepsia, ked chcete mozete si ich pozriet
'''
import time

b = 100000000000000

start = time.monotonic()
def generate_square(n):
    l = [1]
    x = 1
    while n >= (c := l[-1] + (x := x + 2)):
        l.append(c)
    return l

print(generate_square(b))
end1 = time.monotonic() - start


start = time.monotonic()
def generate_square2(n):
    n += 1
    l = [1]
    x = 3
    while n > (c := l[-1] + x):
        l.append(c)
        x += 2
    return l

print(generate_square2(b))
end2 = time.monotonic() - start

start = time.monotonic()
def generate_square3(n):
    l = []
    for i in range(1, n):
        if (a := i ** 2) > n:
            return l
        l.append(a)
    return l
print(generate_square3(b))
end3 = time.monotonic() - start

print(end1)
print(end2)
print(end3)
'''