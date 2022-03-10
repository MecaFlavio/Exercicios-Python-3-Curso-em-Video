# Faça um programa que leia um numero inteiro e diga se ele é ou não
# um numero primo

primo = 0
n = int(input('Um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        primo = primo + 1
if primo == 2:
    print(f'O número {n} é um número PRIMO')
else:
    print(f'O número {n} não é um número PRIMO')
