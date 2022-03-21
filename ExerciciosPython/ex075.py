# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vzs apareceu o número 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

# Coletando entradas em uma tupla
numeros = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')),
           int(input('Digite um numero: ')))
print(f'Os valores digitados foram {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
