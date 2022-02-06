#Faça um programa que leia um angulo qualquer e mostre o valor do seno, coseno e tangente desse angulo

import math

n = float(input('Insira o ângulo: '))
n2 = math.radians(n)
print(f'O cosseno é {math.cos(n2):.2f}, o seno é {math.sin(n2):.2f} e a tangente é {math.tan(n2):.2f}.')
