# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print((5 * '-=-'), 'Analisador de Triangulos', (5 * '-=-'))
m1 = float(input('Digite a primeira medida: '))
m2 = float(input('Digite a segunda medida: '))
m3 = float(input('Digite a terceira medida: '))

print(20 * '-=-')
if m1 + m2 > m3 and m2 + m3 > m1 and m3 + m1 > m2:
    print('As medidas acima podem formar um triangulo!')
else:
    print('A medidas acima não podem formar um triagulo!')
