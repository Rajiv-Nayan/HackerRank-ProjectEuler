from math import factorial as f

def swapPos(x, y):
    for i in range(y , x , -1):
        s[i],s[i-1] = s[i-1], s[i]
def findFact(x, k, pos = 0):
    if (k == 0):
        return
    swapPos(pos, (x - 1) // f(k) + pos)
    findFact( (x - 1)  % f(k) + 1, k - 1, pos + 1)
for _ in range(int(input())):
    n = int(input())
    
    s = list('abcdefghijklm')
    k = len(s) - 1

    findFact(n, k)
    print(''.join(s))
