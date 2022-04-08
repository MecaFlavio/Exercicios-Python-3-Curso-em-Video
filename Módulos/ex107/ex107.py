# Crie um módulo chamado moeda.py que tenha as funçoes incorporadas
# aumentar(), diminuir(), dobro() e medade().
# Faça também um programa que importe esse modulo e use algumas dessas funções.

import moeda

valor = float(input('Digite um valor: '))
print(f'O valor aumentado de {valor} é {moeda.aumentar(valor, 10)}')
print(f'O valor com deconto de {valor} é {moeda.diminuir(valor, 10)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')

