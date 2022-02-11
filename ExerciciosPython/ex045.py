# Crie um programa que faça o computador jogar Jokenpô com você.

import random

print(5 * '=', 'Hora do Jo ken Pô', 5 * '=',
      '''\nPEDRA
PAPEL
TESOURA''')
mão = str(input('Qual a sua escolha: ')).strip().upper()
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print(f'Voce escolheu {mão} e eu escolhi {computador}')
if mão == computador:
    print('Empatamos')
elif (mão == 'PAPEL' and computador == 'PEDRA') or (mão == 'PEDRA' and computador == 'TESOURA') or \
        (mão == 'TESOURA' and computador == 'PAPEL'):
    print('Voce ganhou!')
else:
    print('Voce perdeu!')
