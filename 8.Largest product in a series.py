def compute(num,k):
    ans = max(digit_product(num[i : i + k]) for i in range(len(num) - k + 1))
    return str(ans)
 
 
def digit_product(s):
    result = 1
    for c in s:
        result *= int(c)
    return result
 
 
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(compute(num,k))
