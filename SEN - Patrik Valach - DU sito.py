import random

# 1 - 3 nevytvaraju dalsie polia

def sito1():
    return list(set([random.randrange(0,1000) for i in range(1000)]))
print(sito1())

def sito2():
    pole = [random.randrange(0,1000) for i in range(1000)]
    for i in range(len(pole)-1, -1, -1):
        if pole[i] in pole[:i]:
            pole.pop(i)
    return pole
print(sito2())

def sito3():
    i = 0
    pole = [random.randrange(0,1000) for i in range(1000)]
    while i < len(pole):
        if pole[i] in pole[i+1:]:
            pole.pop(i)
        else:
             i += 1
    return pole
print(sito3())

# skusanie s list comprehension, funguju, ale vytvara to dalsie listy

def sito4():
    pole = [random.randrange(0,1000) for i in range(1000)]
    return [pole.pop(i) for i in range(len(pole)-1, -1, -1) if pole[i] not in pole[:i]]
print(sito4())

def sito5():
    pole = [random.randrange(0,1000) for i in range(1000)]
    return [pole[i] for i in range(len(pole)-1, -1, -1) if pole[i] not in pole[:i]]
print(sito5())

def sito6():
    pole = [random.randrange(0,1000) for i in range(1000)]
    return [pole[i] for i in range(len(pole)) if pole[i] not in pole[i+1:]]
print(sito6())