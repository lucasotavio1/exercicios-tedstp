valores = []

for i in range(100):
    valor = int(input())
    valores.append(valor)

valor_max = max(valores)
max_pos = valores.index(valor_max) + 1

print(valor_max)
print(max_pos)
