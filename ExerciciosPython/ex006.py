## Leia uma numero e mostre o seu dobro, triplo e raiz quadrada
n = float(input('Digite um numero: '))
a = n * 2
b = n * 3
c = n ** (1/2)
print(f'Você digitou {n}, o dobro de {n} é {a}, o triplo é {b} e a raiz quadrada é {c:.2f}')
