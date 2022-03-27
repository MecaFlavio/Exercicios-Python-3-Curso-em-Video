# Faça um programa que leia nome e peso de várias pessoas guardando tudo numa lista. No final mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as mais pesadas
# c) Uma listagem com as pessoas mais leves
lista_max = []
lista_min = []
pesagem = []
lista = []
cont = maior = menor =0
while True:
    pesagem.append(str(input('Nome: ')))
    pesagem.append(float(input('Peso: ')))
    lista.append(pesagem[:])
    pesagem.clear()
    pergunta = str(input('Quer continuar? (S/N): ')).strip().upper()
    while pergunta not in 'SN':
        if pergunta not in 'SN':
            print('Essa resposta é invalida.')
            pergunta = str(input('Quer continuar? (S/N): ')).strip().upper()
    if pergunta in 'N':
        break
print(f'{len(lista)} pessoas foram cadastradas')
for i, v in enumerate(lista):
    if cont == 0:
        maior = menor = v[1]
        cont += 1
    elif v[1] < menor:
        menor = v[1]
    elif v[1] > maior:
        maior = v[1]

# solução proposta pelo professor para mostrar nomes das pessoas com maior peso e menor peso
print(f'O maior peso registrado foi {maior}, Peso de ', end='')
for v in lista:
    if maior == v[1]:
        print(f'{v[0]}; ', end='')
print()
print(f'O menor peso registrado foi {menor}, Peso de ', end='')
for v in lista:
    if menor == v[1]:
        print(f'{v[0]}; ', end='')

# Solução que eu codei para mostrar pessoas com o maior e menor peso
for i, v in enumerate(lista):
    if maior == v[1]:
        lista_max.append(v[0])
    elif menor == v[1]:
        lista_min.append(v[0])
print(f'O menor peso registrado foi {menor}. Paso de {lista_min}')
print(f'O maior peso registrado foi {maior} Peso de {lista_max}')