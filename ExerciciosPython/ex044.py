# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# - à vista dinheiro / cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão 20% de juros
preco = float(input('Qual o valor do produto: '))
print('''Qual a forma de pagamento?
1 - A vista com Dinhiero. 10% de Desconto
2 - A vista no Cartão. 5% de Desconto.
3 - Parcelado. Até 2x sem juros. Acima de 2 parcelas 20% juros.''')
forma_pagamento = int(input('Qual a opção: '))
if forma_pagamento == 1:
    pagamento = preco * 0.90
    print(f'O valor sera de {pagamento:.2f}')
elif forma_pagamento == 2:
    pagamento = preco * 0.95
    print(f'O valor a ser pago será R${pagamento:.2f}')
elif forma_pagamento == 3:
    parcelas = int(input('Em quantas Parcelas: '))
    if parcelas <= 2 and parcelas != 0 and not parcelas < 0:
        pagamento = (preco / parcelas)
        print(f'O valor a ser pago será de R${pagamento:.2f} por parcela. Total de R${preco:.2f}.')
    elif parcelas > 2:
        pagamento = (preco / parcelas) * 1.2
        print(f'O valor a ser pago será de R${pagamento:.2f} por parcela. Total de R${preco * 1.2:.2f}.')
    else:
        print('Impossivel aplicar esse valor de parcelas! Tente novamente.')
else:
    print('Essa opção não existe!')
