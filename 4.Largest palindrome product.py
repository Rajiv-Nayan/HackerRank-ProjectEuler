import sys
pl = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in pl:
            pl.append(a)
pl.sort()
length = len(pl)
 
 
n = int(input())
for _ in range(n):
    a = int(input())
    for i in range(length - 1, -1, -1):
        if pl[i] < a:
            print(pl[i])
            break
