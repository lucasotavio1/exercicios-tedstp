hr_inicio, min_inicio, hr_fim, min_fim = map(int, input().split())

inicio_total_min = hr_inicio * 60 + min_inicio

fim_total_min = hr_fim * 60 + min_fim

if fim_total_min >  inicio_total_min:
    duracao_total_min = fim_total_min - inicio_total_min
else:
    duracao_total_min = (24 * 60 - inicio_total_min) + fim_total_min

duracao_hr = duracao_total_min // 60 
duracao_min = duracao_total_min % 60

print(f'O JOGO DUROU {duracao_hr} HORA(S) E {duracao_min} MINUTO(S)')
