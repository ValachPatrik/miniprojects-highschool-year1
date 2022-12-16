def spawpcase(s):
    x = ''
    for i in s:
        if i >= 'A' and i <= 'Z':
            x = x + chr(ord(i) - ord('A') + ord('a'))
        elif i >= 'a' and i <= 'z':
            x = x + chr(ord(i) + ord('A') - ord('a'))
        else:
            x += i
    return x

print(spawpcase('Hello tHERe123'))

def startswith(s, x):
    for i in range(len(x)):
        if s[i] != x[i]:
            return False
    return True

print(startswith('Hello there', 'Hel'))
print(startswith('Hello there', 'Helo'))