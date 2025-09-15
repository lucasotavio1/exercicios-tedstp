import sys


def check_senha(i):
    senha = i
    if senha == 2002:
        print('Acesso permitido')
        sys.exit()
    else:
        print('Senha Invalida')


while True:
    senha = int(input())
    check_senha(senha)
