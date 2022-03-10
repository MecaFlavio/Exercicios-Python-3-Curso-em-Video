# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
# final, mostre as 10 primeiros termos dessa progressão.

termo_1 = int(input('Qual é o primeiro termo da PA: '))
razao = int(input('Qual é a razão da PA: '))

for n in range(1, 11):
    pa = termo_1 + ((n - 1) * razao)
    print(pa)
