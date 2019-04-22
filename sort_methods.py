def sort_select(a:list):
'''
Сортирует массив методом выбора
'''
  if len(a) <= 1:
    return a
  i = 0
  while i < (len(a)-1):
    for j in range(i+1, len(a)):
      if a[i] > a[j]:
        a[i], a[j] = a[j], a[i]
    i += 1
  return a

def sort_insert(a:list):
'''
Сортирует массив методом вставки
'''
  if len(a) <= 1:
    return a
  for i in range(1,len(a)):
    j = i
    while j > 0 and a[j] < a[j-1]:
      a[j], a[j-1] = a[j-1], a[j]
      j -= 1
  return a

def sort_bubble(a:list):
'''
Сортирует массив методом пузырька
'''
  if len(a) <= 1:
    return a
  for i in range(len(a)-1,0):
    for j in range(i):
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
  return a

def sort_quick(a:list):
'''
Сортирует массив методом Тони Хоара (быстрая сортировка)
'''
  if len(a) <= 1:
    return a
  b = a[0]
  l = []
  r = []
  m = []
  for i in range(len(a)):
    if a[i] < b:
      l.append(a[i])
    elif a[i] > b:
      r.append(a[i])
    else:
      m.append(a[i])
  sort_quick(l)
  sort_quick(r)
  k = 0
  for i in l+m+r:
    a[k] = i
    k += 1
  return a

def sort_merge(a:list):
'''
Сортирует массив методом слияния
'''
  if len(a) <= 1:
    return a
  l = a[:len(a)//2]
  r = a[len(a)//2:]
  sort_merge(l)
  sort_merge(r)
  c = [0] * (len(l)+len(r))
  i = j = k = 0
  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      c[k] = l[i]
      i += 1
    else:
      c[k] = r[j]
      j += 1
    k += 1
  while i < len(l):
    c[k] = l[i]
    i += 1
    k += 1
  while j < len(r):
    c[k] = r[j]
    j += 1
    k += 1
  a[:] = c[:]
  return a

a = [1,2,3,4,5,6]
b = [6,5,4,3,2,1]
c = [1,2,3,6,5,4]
d = [6,5,4,1,2,3]
e = [5,8,10,1,3,4]

print(a,b,c,d, e)
print(sort_select(a), sort_select(b), sort_select(c), sort_select(d), sort_select(e))
print(sort_insert(a), sort_insert(b), sort_insert(c), sort_insert(d), sort_insert(e))
print(sort_bubble(a), sort_bubble(b), sort_bubble(c), sort_bubble(d), sort_bubble(e))
print(sort_quick(a), sort_quick(b), sort_quick(c), sort_quick(d), sort_quick(e))
print(sort_merge(a), sort_merge(b), sort_merge(c), sort_merge(d), sort_merge(e))
