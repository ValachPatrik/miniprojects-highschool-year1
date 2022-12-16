n = int(input('Insert number: '))

h = ''
if n == 0:
    h += 'a'
while (n > 0):
  x = n % 26
  h = chr(ord('a') + x) + h
  n //= 26
print(h)