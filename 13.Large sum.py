import sys

t = int(input())
sum = 0
for _ in range(t):
    n = int(input())
    sum += n
last_sum = str(sum)
print(last_sum[:10])
