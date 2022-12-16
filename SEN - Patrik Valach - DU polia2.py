def nachadza(a, b):
  for i in b:
    if i not in a:
      return False
  return True

a = [1, 2, 4, 5]
b = [1, 2, 1, 2, 1]
print(nachadza(a, b))


def druhe_najmensie(l):
  naj = None
  druhe = None
  for i in l:
    if naj == None or naj > i:
      if druhe != None:
        druhe = naj
      naj = i
    elif druhe == None or druhe > i:
      druhe = i
  return druhe

l = [1, 5, 0, 4, -1, 8, 9, -1]
print(druhe_najmensie(l))


def bonus(l, n):
  for i in range(len(l)):
    if l[i] == n:
      l.append(l.pop(i))
  return l

l = [1, 2, 0, 4, 1, 2, 0, 5, 4, 3, 2, 0]
print(bonus(l,2))