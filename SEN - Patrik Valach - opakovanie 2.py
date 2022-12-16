s = input('str = ')

t = ''
for i in s:
    if ord(i)%3 == 0:
        t += chr(ord('A') + ord(i) - ord('a'))
    else:
        t += i
print(t)