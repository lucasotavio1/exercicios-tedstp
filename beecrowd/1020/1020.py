n = int(input())

anos = n//365
n %= 365

meses = n//30
n %= 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{n} dia(s)')