n = int(input('Zadaj n: '))

for i in range(n,0,-1):
    if i == n:
        print ('x'*(i-1), end='')
    else:
        print ('x'*i, end='')
        print(' '*((n-i)*2-1),end='')
    print ('x'*i, end='')
    print()