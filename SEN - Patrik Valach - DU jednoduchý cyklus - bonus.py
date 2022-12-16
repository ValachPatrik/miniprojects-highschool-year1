n = int(input('Insert a number: '))

for a in range(n):
    if a**2 < n:
        print(str((a**2)) + ', ', end='')