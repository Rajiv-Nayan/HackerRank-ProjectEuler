import sys
import math
 
def compute(n):
    
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return str(n)

def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n  
 
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(compute(n))
