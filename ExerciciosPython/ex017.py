#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa
import math
n1 = float(input('Medida do cateto oposto: '))
n2 = float(input('Medida do cateto adjacente: '))

print(f'A hipotenusa é { math.hypot(n1,n2):.1f}')

## Resolução do professor


