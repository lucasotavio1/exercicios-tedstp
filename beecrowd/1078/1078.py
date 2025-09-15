def tabuada(x):
    for y in range(1, 11):
        resultado = y * x
        print(f'{y} x {x} = {resultado}')

n = int(input())

tabuada(n)
