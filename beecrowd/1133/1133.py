x = int(input())
y = int(input())

if x > y:
    x, y = y, x
for resultado in range(x + 1, y):
    if resultado % 5 == 2 or resultado % 5 == 3:
        print(resultado)
