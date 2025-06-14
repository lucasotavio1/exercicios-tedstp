numero = int(input())

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i
print(f'{fatorial}')