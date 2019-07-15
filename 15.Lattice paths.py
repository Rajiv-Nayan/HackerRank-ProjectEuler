t=int(input())
while t:
    n,m=list(map(int,input().split()))
    j=1
    k=1
    q=1
    r=m+n
    for i in range(1,r+1):
        j=j*i
    for w in range(1,n+1):
        k=k*w
    for e in range(1,m+1):
        q=q*e
    if n>=20 or m>=20  :  
         print(int(j//(k*q))%(10**9+7) ) 
    else:
        print(int(j//(k*q)))
    t -=1
