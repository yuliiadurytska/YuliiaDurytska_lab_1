n = int(input())
afp = 0
bfn = 1
i = 1
fib = 1
while i < n:
    fib = afp + bfn
    afp = bfn
    bfn = fib
    i += 1
print(fib)
