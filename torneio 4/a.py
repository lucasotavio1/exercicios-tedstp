n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        resultado = i ** 2
        print(f'{i}^2 = {resultado}')