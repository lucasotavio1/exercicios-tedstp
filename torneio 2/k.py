x = int(input())
y = int(input())

if x > y:
    x, y = y, x

soma_impares = 0

for i in range (x + 1, y):
    if i % 2 != 0:
        soma_impares += 1
        
print(soma_impares)
