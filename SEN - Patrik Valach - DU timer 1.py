import time

n = int(input('Zadaj n: '))
for i in range (1,n+1):
    for j in range (i):
        print ('*',end='')
        time.sleep(1/i)
    print()