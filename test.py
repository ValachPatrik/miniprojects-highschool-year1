'''
n = int(input('n= '))
t=''
for i in range (n):
    t = t + chr(ord('A')+i)
    print(t)
'''
'''
n = str(input('Zadaj cislo v 8-sustave (A-H): '))

a = 0
mocnina = (len(n)-1)
for i in n:
    if i < 'A' or i > 'H':
        print('Neplatna hodnota.')
        exit()
    a = (ord(i) - ord('A')) * (8**mocnina) + a
    mocnina-=1
print(a)
'''
'''
n = int(input('Zadaj cislo v 10-tkovej sustave: '))
h = ''
if n == 0:
    h = h + 'A'
while (n > 0):
  x = n % 8
  h = chr(ord('A') + x) + h
  n //= 8

print(h)
'''