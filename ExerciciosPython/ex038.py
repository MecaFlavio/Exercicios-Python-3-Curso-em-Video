# Escreva um programa que leia dois numeros inteiros e compare-os mostrando
# na tela uma mensagem
#
#  - O primeiro valor é maior
#  - O segundo valor é maior
#  - Não existe valor maior, os dois são iguais

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))

if numero_1 > numero_2:
    print('O primeiro valor {} é maior que o segundo valor {}.'.format(numero_1, numero_2))
elif numero_1 < numero_2:
    print('O segundo valor {} é maior que o primeiro valor {}.'.format(numero_2,numero_1))
else:
    print('Não existe valor maior, os dois são íguais.')