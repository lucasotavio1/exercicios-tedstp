x = int(input())
y = int(input())
inicio = min(x, y)
fim = max(x, y)

for resultado in range(inicio, fim):
    if resultado % 5 == 2 or resultado % 5 == 3:
        print(resultado)
