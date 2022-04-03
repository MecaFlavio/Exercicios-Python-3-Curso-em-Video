# Faça um programa que tenha uma função chamada contador()
# que receba três paramentros: inicio, fim e passo e realize a contagem
# o programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1.
# b) de 10 até 0, de 2 em 2.
# c) uma contagem personalizada
from time import sleep


def mold():
    print('=' * 30)


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    mold()
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 2, 2)
mold()
print('Agora defina a contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
