# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ('Lapis', 1.15,
         'Borracha', 0.60,
         'Caneta', 1.75,
         'Lapiseira', 7.35,
         'Caderno', 25,
         'Mochila', 75.90,
         'Estojo', 5)
print('-' * 40)
print(f'{"Lista de materiais":^40}')
print('-' * 40)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>6.2f}')
print('-' * 40)
