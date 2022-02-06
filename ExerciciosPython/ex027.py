# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.

nome = str(input('Escreva Seu nome: ')).strip()
a = nome.split()
print('Seu primeiro nome é {}'.format(a[0]))
print('Seu Ultimo nome é: {}'.format(a[len(a)-1]))
print(len(a))# retorna o numero de elementos na lista iniciando de 1

