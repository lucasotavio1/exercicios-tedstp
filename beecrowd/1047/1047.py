hora_inicial, hora_final = map (int, input().split())

if hora_final >= hora_inicial:
    hora_total = hora_final - hora_inicial
else:
    hora_total = (24 - hora_inicial) + hora_final
    
print(f'O JOGO DUROU {hora_total} HORA(S)')
