a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista1 = [a, b, c, d, e, f]

contador = 0

for i in lista1:
    if i > 0:
        contador += 1
        
print(f'{contador} valores positivos')
