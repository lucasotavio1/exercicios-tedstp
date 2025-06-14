nome = input()

salario_fixo = float(input())
total_vendas = float(input())

total = salario_fixo + total_vendas * 0.15

print('TOTAL = R$ {:.2f}'.format(total))