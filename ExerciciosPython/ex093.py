# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado num dicionário, incluindo o total de gols feitos durante o campeonato.
lista_gols = []
dicionario = {}
#soma = 0  # Variavel criada para soma
dicionario['Nome'] = str(input('Nomer do Jogador: '))
tot = int(input(f'Quantas partidas {dicionario["Nome"]} jogou: '))
# Inserindo valores em uma lista
for v in range(0, tot):
    lista_gols.append(int(input(f'Quantos gols na {v + 1}ª partida: ')))
#    soma += lista_gols[v]  # outra forma de fazer soma dos valores da lista, foi utilizado o metodo sum()
# inserindo uma lista em um dicionário
dicionario['Gols'] = lista_gols[:]
dicionario['Total'] = sum(lista_gols)  # forma de somar valores da lista
print('=' * 30)
print(dicionario)
print('=' * 30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
# Manipulando o dicionário e os valores da lista no dicionário
print(f'O jogador {dicionario["Nome"]} jogou {len(dicionario["Gols"])} partidas')
for i, v in enumerate(dicionario["Gols"]):
    print(f'Na Partida {i + 1}ª, fez {v} gols.')
print(f'Foi um total de {dicionario["Total"]} gols.')
