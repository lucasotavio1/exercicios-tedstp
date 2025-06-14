while True:
    n = int(input())

    if n == 0:
        break
    max_val = 2 ** (2 * (n - 1))

    largura = len(str(max_val))

    matriz = [[2 ** (i + j) for j in range(n)] for i in range(n)]

    for linha in matriz:
        print(' '.join(f'{x:>{largura}}' for x in linha))
        
    print()