# Faça um mini-sistema que utilize o interactive Help do python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se
# encerrará
# OBS: use cores.
from time import sleep
cores = ('\33[m',         # 0 - sem cores
         '\33[0;30;41m',  # 1 - vermelho
         '\33[0;30;42m',  # 2 - verde
         '\33[0;30;43m',  # 3 - amarelo
         '\33[0;30;44m',  # 4 - azul
         '\33[0;30;45m',  # 5 - roxo
         '\33[1;107m'      # 6 - branco
         )


def ajuda(com):
    titulo(f'Pesquisando manual de \'{com}\'', 4)
    sleep(1)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('-' * tam)
    print(f'{msg:^{tam}}')
    print('-' * tam)
    print(cores[0], end='')


# programa principal
while True:
    sleep(1)
    titulo('Ajuda PyHELP', 2)
    comando = str(input('função ou bioblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
sleep(1)
titulo('Até logo', 3)

