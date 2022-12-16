print('{:_^23}'.format('{:*>21.3f}'.format(2.2859))) #_****************2.286_
print('{:#x} {:b}'.format(291, 291)) #0x123 100100011
print('{0:+.2f} {1:+.2f} {0:+.2f}'.format(1.23, -1.23)) #+1.23 -1.23 +1.23

n = int(input('Zadaj n: '))
for i in range (1,n+1):
    s = ''
    for j in range (i*2-1):
        s += str(i)
    print('{:^{space}}'.format(s, space=(len(s)+(n-i)*2)))