s = 'Trochu dlhsi string'
t = 'nahrada'
def replace(s,n,t):
    x = ''
    for i in range((len(s))):
        if i >= n and i < n+len(t):
            x += t[i-n]
        else:
            x += s[i]
    return x

print(replace(s, 0, t)) # nahradadlhsi string
print(replace(s, 1, t)) # Tnahradalhsi string
print(replace(s, 7, t)) # Trochu nahradatring
print(replace(s, 15, t)) # Trochu dlhsi stnahr
print(replace(s, 25, t)) # Trochu dlhsi string

def rotateWords(s):
    x = ''
    s = s.split()
    for i in s:
        x += i[::-1] + ' '
    return x
print(rotateWords("string")) # gtirns
print(rotateWords("string je retazec")) # gtirns ej cezater
print(rotateWords("string j ret azec")) # gtirns j ter ceza