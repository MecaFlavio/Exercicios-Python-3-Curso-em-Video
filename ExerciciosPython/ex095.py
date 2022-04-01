# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detelhes do
# aproveitamento de cada jogador
lista_jogadores = []
lista_gols = []
dicionario = {}
while True:
    dicionario.clear()
    lista_gols.clear()
    dicionario['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {dicionario["nome"]} jogou: '))
    # Inserindo valores em uma lista
    for v in range(0, tot):
        lista_gols.append(int(input(f'Quantos gols na {v + 1}ª partida: ')))
    # inserindo uma lista em um dicionário
    dicionario['gols'] = lista_gols[:]
    dicionario['total'] = sum(lista_gols)  # forma de somar valores da lista
    lista_jogadores.append(dicionario.copy())
    while True:
        pergunta = str(input('Quer continuar? (S/N): ')).strip().upper()
        if pergunta in 'SN':
            break
        elif pergunta not in 'SN':
            print('ERRO. Digite apenas S ou N')
    if pergunta in 'N':
        break
print('-=' * 30)
print(f'{"COD":<5}{"NOME":<15}{"GOLS":<15}{"TOTAL":<15}')
print('_' * 30)
for i, v in enumerate(lista_jogadores):
    print(f'{i:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
print()
while True:
    pergunta_2 = int(input('Exibir dados de qual jogador? (999 para parar): '))
    print('=' * 30)
    if pergunta_2 == 999:
        break
    if pergunta_2 >= len(lista_jogadores):
        print(f'Erro. Digite um numero entre 0 e {(len(lista_jogadores) - 1)}, ou digite 999 para sair.')
        print('=' * 30)
    else:
        print(f'O jogador {lista_jogadores[pergunta_2]["nome"]} jogou {len(lista_jogadores[pergunta_2]["gols"])} '
              f'partidas')
        for i, v in enumerate(lista_jogadores[pergunta_2]['gols']):
            print(f'>>>>>> No jogo {i + 1} fez {v} gols')
        print('=' * 30)
print('Ate breve')
