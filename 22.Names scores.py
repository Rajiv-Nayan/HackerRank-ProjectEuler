n=int(input())
l=[]
for i in range(n):
    l.append(input())
l=sorted(l)
m=int(input())
x=[]
for j in range(m):
    x.append(input())
    s=sum(map(ord,x[j]))-(64*len(x[j]))
    p=l.index(x[j])+1
    print(s*p)
