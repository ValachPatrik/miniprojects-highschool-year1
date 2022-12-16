n = int(input('Zadaj n= '))
k = 0
for i in range (n*2-1):
    if i < n:
        k += 1
    else:
        k -= 1
    for j in range (n-k):
        print (' ', end='')
    print('#', end='')
    for j in range (k*2-2):
        print ('#', end='')
    print()
