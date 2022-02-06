# Um professor quer sortear um dos seu quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

import random

n1 = str(input('Escreva nome 1: '))
n2 = str(input('Escreva nome 2: '))
n3 = str(input('Escreva nome 3: '))
n4 = str(input('Escreva nome 4: '))
nomes = n1,n2,n3,n4 #não serve pra nada kkkk

print('O nome escolhido é:', random.sample([n1,n2,n3,n4],k=1))
print('A ordem será', random.sample([n1,n2,n3,n4], k=4))

## Resolução do professor

n1 = str(input('Escreva nome 1: '))
n2 = str(input('Escreva nome 2: '))
n3 = str(input('Escreva nome 3: '))
n4 = str(input('Escreva nome 4: '))

lista = [n1, n2, n3, n4] # dessa forma se cria uma lista, entre colchetes [].

escolhido = random.choice(lista)
print(escolhido)
