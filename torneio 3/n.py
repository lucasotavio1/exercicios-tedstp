operacao = input().strip()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0

contador = 0

for i in range(12):
    for j in range(i):
        soma += matriz[i][j]
        contador += 1
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / contador
    print(f"{media:.1f}")