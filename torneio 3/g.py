n = int(input())

a = 0
b = 1

sequencia_fib = []

for i in range(n):
    if i == 0:
        sequencia_fib.append(a)
    elif i == 1:
        sequencia_fib.append(b)
    else:
        fib = a + b
        a = b
        b = fib
        sequencia_fib.append(fib)
        
print(" ".join(map(str, sequencia_fib)))