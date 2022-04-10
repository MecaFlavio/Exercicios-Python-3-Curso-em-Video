# aula 022 - Modulos e Pacotes
from uteis import numeros  # importei as funçoes que estão na pasta uteis e pasta numeros
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')

