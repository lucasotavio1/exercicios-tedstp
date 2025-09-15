valor = []

valores_positivos = 0

for _ in range(6):
    valor.append(float(input()))

valores_positivos = [i for i in valor if i > 0]

print(f'{len(valores_positivos)} valores positivos')
print(f'{sum(valores_positivos) / len(valores_positivos):.1f}')