#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome tem Silva? {nome.upper().count("SILVA") >= 1}.')

# Resolução do Professor

nome = str(input('Qual é o seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) # in verifica se existe a string na frase inserida.