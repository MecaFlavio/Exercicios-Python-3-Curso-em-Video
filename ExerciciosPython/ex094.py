# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa num dicionário
# numa lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média

lista = []
dicionário = {}
soma = média = 0
while True:
    dicionário.clear()
    dicionário['nome'] = str(input('Nome: '))
    while True:
        dicionário['sexo'] = str(input('sexo:(M/F) ')).strip().upper()
        if dicionário['sexo'] in 'MF':
            break
        else:
            print('Erro. Digite apenas M ou F')
    dicionário['idade'] = int(input('idade: '))
    soma += dicionário['idade']
    lista.append(dicionário.copy())
    while True:
        pergunta = str(input('Quer continuar: (S/N) ')).strip().upper()
        if pergunta in 'SN':
            break
        elif pergunta not in 'SN':
            print('ERRO. Digite apenas (S/N).')
    if pergunta in 'N':
        break
média = soma / len(lista)
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoaa.')
print(f'A media de idade do grupo é de {média} anos.')
print('As mulheres cadastradas foram:')
for d in lista:
    if d['sexo'] == 'F':
        print(f'{d["nome"]}; ', end='')
print()
print('As pessoas acima da média de idade do grupos são:')
for d in lista:
    if d['idade'] > média:
        print('   ', end='')
        for k, v in d.items():
            print(f'{k} = {v} ', end='')
        print()
print('Encerrado')

