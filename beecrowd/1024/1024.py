def criptografar(msg):
    primeira_passada = []
    for char in msg:
        if 'a' <= char <= 'z':
            primeira_passada.append(chr(ord(char) + 3))
        elif 'A' <= char <= 'Z':
            primeira_passada.append(chr(ord(char) + 3))
        else:
            primeira_passada.append(char)
    segunda_passada = ''.join(primeira_passada)[::-1]

    metade = len(segunda_passada) // 2
    
    resultado = []

    for i in range(len(segunda_passada)):
        char = segunda_passada[i]
        if i >= metade and ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            resultado.append(chr(ord(char) - 1))
        else:
            resultado.append(char)
    return ''.join(resultado)


def entradas(n, mensagens):
    for msg in mensagens:
        print(criptografar(msg))


N = int(input())

mensagens = [input().strip() for _ in range(N)]

entradas(N, mensagens)
