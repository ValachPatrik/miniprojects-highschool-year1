import time

def bonus(l, n):  #funguje
  for i in range(len(l)):
    if l[i] == n:
      l.append(l.pop(i))
  return l

def bonus2(l, n):
    l2 = []
    pocet = 0
    for i in l:
        if i != n:
            l2.append(i)
        else:
            pocet += 1
    for i in range (pocet):
        l2.append(n)
    return l2

def bonus3(l, n):  #funguje
  for e, i in enumerate(l):
    if i == n:
      l.append(l.pop(e))
  return l




li = [1, 2, 0, 4, 1, 2, 0, 5, 4, 3, 2, 0]
nn = 2


start = time.monotonic()
print(bonus(li, nn)) 
end1 = time.monotonic() - start
print(end1)

start = time.monotonic()
print(bonus2(li, nn)) 
end2 = time.monotonic() - start
print(end2)

start = time.monotonic()
print(bonus3(li, nn)) 
end3 = time.monotonic() - start
print(end3)