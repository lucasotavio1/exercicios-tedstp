notas = []

while len(notas) < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print('nota invalida')

media = sum(notas) / 2

print(f'media = {media:.2f}')