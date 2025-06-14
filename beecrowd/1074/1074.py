contador = 0

n = int(input())

valores = []

while contador < n:
    valor = int(input())
    valores.append(valor)
    contador += 1

for i in valores:
    if i % 2 == 0 and i > 0:
        print('EVEN POSITIVE')
    if i % 2 != 0 and i > 0:
        print('ODD POSITIVE')
    if i % 2 == 0 and i < 0:
        print('EVEN NEGATIVE')
    if i % 2 != 0 and i < 0:
        print('ODD NEGATIVE')
    if i == 0:
        print('NULL')
