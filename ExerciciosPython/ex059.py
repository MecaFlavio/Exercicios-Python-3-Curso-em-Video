# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 soma
# 2 muntiplicar
# 3 maior
# 4 novos numeros
# 5 sair do programa
# seu programa devera relalizar a operação solicitada em cada caso.
import time
import os
opcao = 0
numero_1 = float(input('Digite o 1º numero: '))
numero_2 = float(input('Digite o 2º numero: '))
while opcao != 5:
    print('''O que deseja realizar?
[1] - Somar
[2] - Multiplicar
[3] - Saber o Maior
[4] - Novos Numeros
[5] - Sair do programa''')
    opcao = int(input('Digite o numero da opção: '))
    if opcao == 1:
        soma = numero_1 + numero_2
        print(soma)
        time.sleep(2)
    elif opcao == 2:
        multi = numero_1 * numero_2
        print(multi)
        time.sleep(2)
    elif opcao == 3:
        maior = numero_1
        if numero_2 > numero_1:
            maior = numero_2
        print(maior)
        time.sleep(2)
    elif opcao == 4:
        time.sleep(2)
        print('Digite Novos Numeros:')
        numero_1 = float(input('Digite o 1º numero: '))
        numero_2 = float(input('Digite o 2º numero: '))
    elif opcao == 5:
        print('Obrigado e até logo!!')
    else:
        time.sleep(1)
        print('Essa opção não existe')
        time.sleep(1)
