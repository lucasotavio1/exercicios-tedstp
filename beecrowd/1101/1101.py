import sys


while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        sys.exit()

    lista = list(range(min(m, n), max(m, n) + 1))

    soma = sum(lista)
    
    print(f"{' '.join(map(str, lista))} Sum={soma}")
