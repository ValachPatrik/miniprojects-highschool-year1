s = '123456789'
for i in range(1,len(s)+1):
    print(s[-i:])

s = '9876543210123456789'
for i in range(len(s)//2+1):
    print('{:^{len}}'.format(s[len(s)//2-i:len(s)//2+1+i], len=len(s)))
