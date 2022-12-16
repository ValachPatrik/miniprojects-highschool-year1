n = int(input('Insert n: '))
k = 0
for i in range (n):
    for j in range (i+1):
        print (chr(ord('A')+k), end='')
        k += 1
        if k == (ord('Z')-ord('A')+1):
            k = 0
    print()