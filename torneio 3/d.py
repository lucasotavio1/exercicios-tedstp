while True:
    x, y = map(int, input().split())
    if x == y:
        break
    if x > y:
        print('Decrescente')
    elif y > x:
        print('Crescente')