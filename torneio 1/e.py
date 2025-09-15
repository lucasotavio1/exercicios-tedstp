dia_inicio = int(input().split()[1])

hora_inicio, min_inicio, seg_inicio = map(int, input().split(' : '))

dia_fim = int(input().split()[1])

hora_fim, min_fim, seg_fim = map(int, input().split(' : '))

incio_total_seg = (dia_inicio * 86400) + (hora_inicio * 3600) + (min_inicio * 60) + seg_inicio

fim_total_seg = (dia_fim * 86400) + (hora_fim * 3600) + (min_fim * 60) + seg_fim

duracao_total_seg = fim_total_seg - incio_total_seg

dias = duracao_total_seg // 86400
resto = duracao_total_seg % 86400
horas = resto // 3600
resto %= 3600
minutos = resto // 60
segundos = resto % 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
