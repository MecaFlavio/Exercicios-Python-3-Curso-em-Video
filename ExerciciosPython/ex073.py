# Crie uma tupla preenchida com os 20 primeiros colocados da tabela o campeonato brasileiro, na ordem de colocação
# Depois mostre
# a) Apenas os 5 primeiros colocados
# b) Os últimos 4 colocados da tabela
# c) Uma lista com os times em ordem alfabética
# d) Em que posição na tabela está o time da chapecoence

# Tentei aplicar conhecimentos de aulas anteriores a essa atividade

# Criação da tupla com colocação do campeonato brasieleiro de 2021
colocação = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Conrinthians', 'Bragantino', 'Fluminense',
             'América - MG', 'Atletico - GO', 'Santos', 'Ceará', 'Intenacional', 'São Paulo', 'Athletico - PR',
             'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

# Defini uma variavel simples com string de moldura para facilitar a visualisação
cabeçalho = '-=' * 30

print(cabeçalho)
print('{:^60}'.format('Campeonato Brasileiro 2021'))
print(cabeçalho)

# Apliquei um looping infinito para dar continuidade no programa
while True:
    print('''O que quer ver:
1 - Os 5 primeiros colocados
2 - Os 4 últimos colocados
3 - Os times em ordem alfabética
4 - A posição da chapecoense''')
    opção = int(input('Escolha a opção desejada: '))
    # esrtrutura para repetir se o usuario colocar opção inexistente
    while opção < 1 or opção > 4:
        print('Essa opção não existe. Tente novamente')
        opção = int(input('Escolha a opção desejada: '))
    # Definição das opções e tratamento da tupla, proposta do exercicio
    if opção == 1:
        print(cabeçalho)
        print('Os 5 primeiros colocados são', colocação[:5])
    elif opção == 2:
        print(cabeçalho)
        print('Os quatro ultimos colocados são', colocação[-4:])
    elif opção == 3:
        print(cabeçalho)
        print('Os times me ordem alfabética são\n', sorted(colocação))
    elif opção == 4:
        print(cabeçalho)
        print(f'A Chapecoense é a {colocação.index("Chapecoense") + 1}ª colocada')
    print(cabeçalho)
    finalizar = ' '
    # Controle para usuiário parar o programa
    while finalizar not in 'SN':
        finalizar = str(input('Quer continuar? (S/N): ')).strip().upper()
        if finalizar not in 'SN':
            print('Essa resposta está incorreta. Tente novamente')
            print(cabeçalho)
    if finalizar == 'N':
        break

