#leia a Largura e a latura de uma parede em metros e calcule a sua area a a quantidade
# Necessaria para pintala, sabendo que a cada litro de tinta pinta uma area de 2m²
#
al = float(input('Digite a altura: '))
la = float(input('Digite a largura: '))
a = al * la
t = a / 2
print(f'A area da parede é de {a:.2f}m²'
      f'\nE a quantidade de tinta a ser usada é de {t:.2f} litros')