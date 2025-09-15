valor = float(input())

valor_inicial = valor

n = int(valor * 100)
notas100 = n//10000
n %= 10000
notas50 = n//5000
n %= 5000
notas20 = n//2000
n %= 2000
notas10 = n//1000
n %= 1000
notas5 = n//500
n %= 500
notas2 = n//200
n %= 200
moedas1 = n//100
n %= 100
moedas50 = n//50
n %= 50
moedas25 = n//25
n %= 25
moedas10 = n//10
n %= 10
moedas5 = n//5
n %= 5
moedas1_cent = n

print(f'NOTAS:')
print(f'{notas100} nota(s) de R$ 100.00')
print(f'{notas50} nota(s) de R$ 50.00')
print(f'{notas20} nota(s) de R$ 20.00')
print(f'{notas10} nota(s) de R$ 10.00')
print(f'{notas5} nota(s) de R$ 5.00')
print(f'{notas2} nota(s) de R$ 2.00')

print(f'MOEDAS:')
print(f'{moedas1} moeda(s) de R$ 1.00')
print(f'{moedas50} moeda(s) de R$ 0.50')
print(f'{moedas25} moeda(s) de R$ 0.25')
print(f'{moedas10} moeda(s) de R$ 0.10')
print(f'{moedas5} moeda(s) de R$ 0.05')
print(f'{moedas1_cent} moeda(s) de R$ 0.01')
