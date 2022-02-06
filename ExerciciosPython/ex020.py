# O mesmo professor quer sortear a ordem de apresentação de trabalhos do alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input('Escreva nome 1: '))
n2 = str(input('Escreva nome 2: '))
n3 = str(input('Escreva nome 3: '))
n4 = str(input('Escreva nome 4: '))
nomes = n1,n2,n3,n4 # também não serve pra nada

print('A ordem será', random.sample([n1,n2,n3,n4], k=4))

## Resolução do professor

n1 = str(input('Escreva nome 1: '))
n2 = str(input('Escreva nome 2: '))
n3 = str(input('Escreva nome 3: '))
n4 = str(input('Escreva nome 4: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)
