# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for impar desconsidera-lo

soma = 0
for c in range(0, 6):
    n = int(input('Um número: '))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares é {}'.format(soma))
