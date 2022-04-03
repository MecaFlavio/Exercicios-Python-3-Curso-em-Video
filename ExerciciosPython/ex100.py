# Faça um programa que tenha uma lista chamada numeros e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# coloca-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sortenados pela função anterior

from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for v in range(0, 5):
        lista.append(randint(0, 10))
        sleep(0.3)
        print(f'{lista[v]} ', end='')
    print('Pronto')


def somapar():
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista} temos o total de {soma}')


lista = []
sorteia()
somapar()

