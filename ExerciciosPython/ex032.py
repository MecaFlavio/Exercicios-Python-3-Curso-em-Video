# faça um programa que leia uma ano qualquer e mostre se ele é bissexto
from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year # pega data atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano Bissexto!')
else:
    print(f'O ano {ano} não é um ano bissexto')
