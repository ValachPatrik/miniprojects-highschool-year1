number = input('Insert yt id: ')
result = 0
mocnina = len(number)-1
for i in number:
    if i >= 'A' and i <= 'Z':
        result = result + (ord(i) - ord('A')) * 64 ** mocnina
    elif i >= 'a' and i <= 'z':
        result = result + (ord(i) - ord('a') + 26) * 64 ** mocnina
    elif i >= '0' and i <= '9':
        result = result + (ord(i) - ord('0') + 52) * 64 ** mocnina
    elif i == '-':
        result = result + 62 * 64 ** mocnina
    elif i == '_':
        result = result + 63 * 64 ** mocnina
    mocnina -= 1
print ('result =', int(result))