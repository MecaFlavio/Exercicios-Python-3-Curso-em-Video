# Crie um programa que leia o nome e o preço de vários produtos. O programa devera perguntar
# se o utilizador vai continuar. No final, mostre:
#
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de 1000 reais
# c) Qual é o nome do produto mais barato
nome_barato = ' '
cont_produtos = preço_barato = total = quant_1000 = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('preço do produto: R$ '))
    total += preço
    cont_produtos += 1
    if preço > 1000:
        quant_1000 += 1
    if cont_produtos == 1 or preço < preço_barato:
        nome_barato = produto
        preço_barato = preço
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar (S/N): ')).strip().upper()
    if resposta == 'N':
        break
print('========= FIM DAS COMPRAS ===========')
print(f'Total gasto: {total}')
print(f'Produtos que custam mais de R$ 1000,00: {quant_1000} produtos')
print(f'O roduto mais barato foi: {nome_barato}')
