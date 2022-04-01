# Variaveis compostas -  Dicionarios
dicionario = {}  # forma de declarar um dicionário
dicionario2 = dict()  # outra forma de declara um dicionário
# Declarando um dicionário com valores
pessoas = {'nome': 'flavio', 'sexo': 'M', 'idade': 32}
print(pessoas)
# Selecionando dados no dicionario
print(pessoas['nome'])
print(pessoas['sexo'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# Manipulando apenas as chaves
print(pessoas.keys())
# Manipulando apenas os valores
print(pessoas.values())
#  Manipulando os itens (chaves e valores)
print(pessoas.items())
# Utilizando laços nos dicionários
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k in pessoas.items():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
# Deletando itens do dicionario
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
# Alterando valores das chaves do dicionário
pessoas['nome'] = 'leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
# Adicionando itens ao dicionário
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
# Criação de listas de dicionários
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
# Manipulando Listas de dicionários
print(brasil[0])  # Mostra o dicionário no indice 0
print(brasil[1])  # mostra o dicionário no indice 1
print(brasil[0]['uf'])  # retorna o valor da chave 'uf' no dicionário 0
print(brasil[1]['sigla'])  # retorna o valor sigla no dicionário 1

estado = dict()
brasil2 = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil2.append(estado.copy())  # Maneira e copiar dicionário sem viculo de listas
print(estado)
print(brasil2)
for d in brasil2:
    for k, v in d.items():
        print(f'A key {k} tem valor {v}.')
for d in brasil2:
    for v in d.values():
        print(v, end=' ')
    print()
