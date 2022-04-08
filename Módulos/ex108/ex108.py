# Adapte o codigo do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.

import moeda

valor = float(input('Digite um valor: R$  '))
print(f'O valor aumentado de {moeda.moeda(valor)} é {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'O valor com deconto de {moeda.moeda(valor)} é {moeda.moeda(moeda.diminuir(valor, 10))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')

