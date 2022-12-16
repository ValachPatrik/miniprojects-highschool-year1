base = [i for i in 'abcdefghijklmnopqrstuvwxyz1234567890 ,.:<>";?!@$%^&*()[]{\}=-+']
key  = [i for i in 'refibmagcwvnqpsuoljyzxdthk2701853469>"*.%?-\}@,^:=[!)<]+ ${&(;']

def encode(text, base = base, key = key):
    text = text.lower()
    out = ''
    posun = 0
    for i in text:
        char_index = base.index(i)
        if char_index + posun <= (len(key) -1):
            out += key[char_index + posun]
        else:
            pocet = (char_index + posun) // (len(key))
            out += key[(char_index + posun) - pocet * (len(key))]
        posun += 1
    return out


def decode(text, base = key, key = base):
    text = text.lower()
    out = ''
    posun = 0
    for i in text:
        char_index = base.index(i)
        if char_index + posun >= 0:
            out += key[char_index + posun]
        else:
            pocet = (-(char_index + posun)) // (len(key))
            out += key[(char_index + posun) + (pocet * (len(key)))]
        posun -= 1
    return out

#print(encode('muu'))
#print(decode(r'quo'))

print(encode('milujem ta laska moja <3'))
print(decode(r'pwa.mylu}7du:sj%)39t*%d}6=ee,=b[,gr'))