
import math
def compute(n):
    ans = 1
    for i in range(1, n+1):
        ans *=i// math.gcd(i, ans)
    return str(ans)
 
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(compute(n))
