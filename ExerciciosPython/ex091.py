# Faça um programa onde 4 jogadores jogue um dado e tenham resultados aleatórios;
# guarde todos esses resultados num dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter  # lib que manipula itens do dicionario
lista = []
lista2 = []
ranking = []
dicionário = {'jog1': randint(1, 6), 'jog2': randint(1, 6), 'jog3': randint(1, 6),
              'jog4': randint(1, 6)}
# criando lista com itemgetter para organizar keys e valores dos dicionários.
ranking = sorted(dicionário.items(), key=itemgetter(1), reverse=True)
print(type(ranking))
for k, v in dicionário.items():
    print(f' O {k} tirou {v} no dado')
    sleep(1)
print('=' * 10, 'Ranking', '=' * 10)
for i, v in enumerate(ranking):
    print(f'{i + 1}ª lugar: {v[0]} com {v[1]}.')
    sleep(1)