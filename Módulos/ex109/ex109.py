# modifique as funçoes que foram criadas no desafio 107 para aceitarem
# um parametro a mais, informando se o valor retornado por eles vai ser ou não formatado
# pela função moeda(), desenvolvida no desafio 108.

import moeda

valor = float(input('Digite um valor: R$  '))
print(f'O valor aumentado em 10% de {moeda.moeda(valor)} é {moeda.aumentar(valor, 10, f=True)}')
print(f'O valor com deconto de 10% de {moeda.moeda(valor)} é {moeda.diminuir(valor, 10, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')

