def fun(s):
    s=str(s)
    tot=0
    for i in range(len(s)):
        tot+=int(s[i])
    return(tot)    
        
num=int(input())
for i in range(num):
    n=int(input())
    s=2**(n)
    print(fun(s))
