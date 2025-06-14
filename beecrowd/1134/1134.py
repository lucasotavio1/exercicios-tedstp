qtd_alcool = 0
qtd_gasolina = 0
qtd_diesel = 0

while True:
    opcao = int(input())
    if opcao == 1:
        qtd_alcool += 1
    elif opcao == 2:
        qtd_gasolina += 1
    elif opcao == 3:
        qtd_diesel += 1
    elif opcao == 4:
        break
    else:
        continue

print('MUITO OBRIGADO')
print(f'Alcool: {qtd_alcool}')
print(f'Gasolina: {qtd_gasolina}')
print(f'Diesel: {qtd_diesel}')
