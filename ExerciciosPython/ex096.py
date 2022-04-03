# Faça um programa que tenha uma função chamada area(),
# que receba as dimenções de um terreno retangular (Largura e comprimento)
# e mostre a area do terrreno.

def moldura(txt):
    print(f'{txt:^30}')
    print('-' * 30)


def area(l, c):
    a = l * c
    print(f'A área do terreno de {l:.1f}mx{c:.1f}m é de {a:.1f}m²')


moldura('Controle de terrenos')
area(float(input('LARGURA(m): ')), float(input('COMPRIMENTO(m): ')))
