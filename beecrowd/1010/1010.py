cod1, qtd1, valor_uni1 = input().split()

cod1 = int(cod1)
qtd1 = int(qtd1)

valor_uni1 = float(valor_uni1)

cod2, qtd2, valor_uni2 = input().split()

cod2 = int(cod2)
qtd2 = int(qtd2)

valor_uni2 = float(valor_uni2)

total = qtd1 * valor_uni1 + qtd2 * valor_uni2

print('VALOR A PAGAR: R$ {:.2f}'.format(total))