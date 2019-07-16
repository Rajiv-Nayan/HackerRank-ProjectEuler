dig_len = dict()
dig_len[1] = 0
length = 2

fib = dict()
fib[0] = 0
fib[1] = 1

def find_fib(x):
    if x < 2:
        return x;
    else:
        no = fib.get(x,-1)
        if no !=-1:
            return no
        else:
            fib[x] = find_fib(x-1) + find_fib(x-2)
            
    return fib[x]

for no in range(1,25000):
    
    op = find_fib(no)
    if len(str(op)) == length:
        dig_len[length] = no
        length += 1
    
t = int(input())

for i in range(t):
    
    no = int(input())
    print(dig_len[no])
