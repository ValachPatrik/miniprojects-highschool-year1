'''
# Tuto funkci implementuj.
def my_abacus(base: int, exp: int) -> int:
    global x
    if exp == 0:
        return 0
    else:
        for i in range(base):
            x += n
    return x + my_abacus(base, exp-1)
# Testy:
print(my_abacus(10, 2))  # 100
print(my_abacus(34, 3))  # 39 304
print(my_abacus(8, 5))  # 32 768
print(my_abacus(2, 10))  # 1024
'''
