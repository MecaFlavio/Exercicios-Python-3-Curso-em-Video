# Crie um programa que vai gerar cinco números aletórios e colocar em uma tupla.
# Depois disso, mostra a listagem de números gerados e também indique e também indique
# o menor e o maior valor que estão na tupla

import random

num1 = num2 = num3 = num4 = num5 = 0
for c in range(0, 5):
    comp = random.randint(0, 10)
    if c == 0:
        num1 = comp
    elif c == 1:
        num2 = comp
    elif c == 2:
        num3 = comp
    elif c == 3:
        num4 = comp
    elif c == 4:
        num5 = comp
tupla = (num1, num2, num3, num4, num5)
print(f'lista de numeros gerados foi {tupla}')
maior = tupla[0]
menor = tupla[0]
for c in range(0, 5):
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
print(f'O numero maior foi {maior} e o numero menor foi {menor}')

# Resolução do professor

# Maneira de coletar entradas em uma tupla
numeros = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
           random.randint(0, 10), random.randint(0, 10))
print('Os Valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')
