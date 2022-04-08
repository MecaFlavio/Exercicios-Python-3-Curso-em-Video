# Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados
# moeda e dados. Tranfira todas as funçoes utilizadas nos desafios 107, 108, 109
# para o primeiro pacote e mantenha tudo funcionando.
from utilidadescev import moeda

valor = float(input('Digite um valor: R$  '))
moeda.resumo(valor, 5, 5)
