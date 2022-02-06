# Escreva um programa que faça o computador "Pensar"
# em um numero inteiro entre 0 e 5 e peça para o uasuario
# tentar descobrir qual foi o numero escolhido pelo computador.
# O programa devera escolher na tela se o usuario venceu ou perdeu.

import random

aposta = int(input('Adivinhe um numero entre 0 e 5: '))
n = random.randrange(6)
print('Sorteando um número...')
if n == aposta:
    print('Parabéns voce acertou! O numero escolhido foi {}'.format(n))
else:
    print(f'O numero escolhido foi {n}. Não foi dessa vez...')

# Resolução do professor
import time

computador = random.randint(0,5) #sorteia um numero conforme o argumento
print("-=-" * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print("-=-" * 20)
print('Pensando...')
time.sleep(3)
print('Pensei!!')
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('Parabens! Você Ganhou eu pensei em {}'.format(computador))
else:
    print('Você não acertou, eu pensei em {} e não em {}. '
          '\nTente novamente!'.format(computador, jogador))

