salario = float(input())

if salario <= 400:
    reajuste = salario * 0.15

    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 15 %')
elif 400.01 <= salario <= 800:
    reajuste = salario * 0.12

    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 12 %')
elif 800.01 <= salario <= 1200:
    reajuste = salario * 0.10

    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 10 %')
elif 1200.01 <= salario <= 2000:
    reajuste = salario * 0.07

    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 7 %')
elif salario > 2000:
    reajuste = salario * 0.04

    novo_salario = salario + reajuste
    
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 4 %')
