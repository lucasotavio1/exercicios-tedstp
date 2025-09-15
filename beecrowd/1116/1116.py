n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    try:
        x / y
    except ZeroDivisionError:
        print('divisao impossivel')
    else:
        print(x/y)
