# Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros
# O programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep


def maior(* num):
    m = c = 0
    print('=' * 30)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='')
        c += 1
        sleep(0.5)
        if c == 1 or v > m:
            m = v
    print(f'Foram informados {c} valores ao todo.')
    print(f'O maior valor foi {m}')


maior(1, 4, 5)
maior(5, 6, 79, 56, 5)
maior(7)
maior()



