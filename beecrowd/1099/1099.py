contador = 0

n = int(input())

while contador < n:
    x, y = map(int, input().split())

    contador += 1
    if x > y:
        x, y = y, x

    soma = 0

    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i
            
    print(soma)
