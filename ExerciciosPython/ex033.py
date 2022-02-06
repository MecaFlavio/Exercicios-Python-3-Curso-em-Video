# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Numero a '))
b = int(input('Numero b '))
c = int(input('Numero c '))
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O numero maior é {maior}')
print(f'O numero menor é {menor}')
