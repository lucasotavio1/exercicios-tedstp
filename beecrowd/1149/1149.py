valores = list(map(int, input().split()))

a = valores[0]

n = 0

for valor in valores[1:]:
    if valor > 0:
        n = valor
        break

soma = sum(a + i for i in range(n))

print(soma)
