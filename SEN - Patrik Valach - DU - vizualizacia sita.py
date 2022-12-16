def sito(n):
    a = [i for i in range(n)]

    print ('0.', end=' ')
    for i in a:
        print(str(i), end=' ')
    print ()
    c = 1

    for i in range(n):
        if i == 0 or i == 1:
            a[i] = None
        elif a[i] != None:
            for j in range(a[i] * 2, len(a), a[i]):
                a[j] = None

        if a[i] != None or i == 0 or i == 1:
            print(str(c) +'. ', end='')
            for j in a:
                if j == None:
                    print('X', end=' ')
                elif j <= i:
                    print('*' + str(j) + '*', end=' ')
                else:
                    print(str(j), end=' ')
            c += 1
            print()

    return [i for i in a if i != None]
#print(sito(100))
#print(sito(20))

def sito2(n):
    MAX = 10000
    num_prime = 1
    a = [i for i in range(MAX)]

    for i in range(MAX):
        if num_prime > n:
            return [j for j in a[:i] if j != None]
        elif i == 0 or i == 1:
            a[i] = None
        elif a[i] != None:
            num_prime += 1
            for j in range(a[i] * 2, len(a), a[i]):
                a[j] = None
#print(sito2(100))
def sito3(n):
    assert n > 0
    x = 2
    poc_prv = 0
    primes = []
    while poc_prv < n:
        je_prv = True
        for i in range(2, x):
            if x % i == 0:
                je_prv = False
        if je_prv:
            poc_prv += 1
            primes.append(x)
        x += 1
    return primes
print(sito3(100))