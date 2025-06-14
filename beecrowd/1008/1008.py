number = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salary = horas_trabalhadas * valor_hora

print('NUMBER =', number)
print('SALARY = U$ {:.2f}'.format(salary))