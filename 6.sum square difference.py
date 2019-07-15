def sqrsum(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+(i*i)
    return sum
def sumsqr(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i
    return(sum*sum)
 
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumsqr(n)-sqrsum(n))
