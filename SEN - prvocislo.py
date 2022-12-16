def prvocislo():
    n = int(input('Zadaj cislo: '))
    if n > 1:
        for i in range (2, n):
            if (n % i) == 0:
                return False
    return True
print(prvocislo())
