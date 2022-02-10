# Refaça o desafio 35 dos triangulos acrecentando o recurso de mostrar
# que tipo de triangulo sera formado:
#
# - Equilatero: Todos os lados iguais
# - Isosceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

lado_1 = float(input('Primeira Medida: '))
lado_2 = float(input('Segunda Medida: '))
lado_3 = float(input('Terceira Medida: '))

# Testa se as retas formam um triangulo
if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_3 + lado_1 > lado_2:
    print('Essas medidas FORMAM um triângulo!')
    if (lado_1 + lado_2 + lado_3) / 3 == lado_1:  # Testa se é equilátero
        print('E esse triangulo é EQUILÁTERO.')
    elif lado_1 == lado_2 != lado_3 or lado_2 == lado_3 != lado_1 or lado_1 == lado_3 != lado_2:  # Testa se é Isosceles
        print('Este triangulo é ISOSCELES')
    elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:  # Testa se é Escaleno
        print('Este triangulo é ESCALENO')
else:
    print('Essas retas não formam um triangulo')
