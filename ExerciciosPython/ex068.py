# Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no
# final do jogo.

import random

vitórias = 0
while True:
    print(20 * '=', '\nJOGO DO PAR OU ÍMPAR\n', 20 * '=')
    numero = int(input('Escolha um numero: '))
    computador = random.randrange(11)
    resposta = str(input('O numero é par ou impar?(P/I): ')).strip().upper()
    soma = computador + numero
    if resposta in 'PI':  # verifica se a resposta é exatamente uma dessas letras ou as duas, na sequencia.
        print(20 * '=')
        print(f'O numero escolhido foi {computador}!'
              f'\nE a soma foi {soma}')
        paridade = soma % 2
        if paridade == 0 and resposta == 'P':
            print('Você acertou! O número é par.')
            vitórias += 1
        elif paridade == 1 and resposta == 'I':
            print('Você acertou! O número é Ímpar.')
            vitórias += 1
        else:
            print('GAME OVER!!! Voce errou!')
            print(f'Você acertou {vitórias} vezes!')
            break
    else:
        print('Essa opção não existe. Tente novamente.')
