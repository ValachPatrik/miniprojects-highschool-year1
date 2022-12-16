a = int(input('Insert first number: '))
b = int(input('Insert second number: '))

for c in range (1,(a+1)):
    if c % b != 0:
        print (str(c)+', ', end='')