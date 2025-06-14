import math


def cal_raiz(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 'A equação não possui raízes'
    elif delta == 0:
        raiz = -b/(2*a)
        return f'A equação possui uma raíz: {raiz}'
    else:
        raiz1=(-b + math.sqrt(delta))/(2*a)
        raiz2=(-b - math.sqrt(delta))/(2*a)
        return f'As raízes da equação são:  {raiz1} e {raiz2}'
    
x, y, z = map(float, input("Digite os valores da equação: ").split())

resultado =  cal_raiz(x, y, z)

print(resultado)
