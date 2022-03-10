# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
# No final do progrma, mostre:
#
# - A média de idade do grupo
# - O nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos

nome_velho = ''
idade_maior = 0
soma = 0
cont_media = 0
cont_feminino = 0
for c in range(1, 5):
    nome = str(input('Qual seu nome: ')).strip().upper()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo '
                     '\n(F) para feminino'
                     '\n(M) para masculino: ')).strip().upper()
    soma += idade
    cont_media += 1
    if idade > idade_maior and sexo == 'M':
        idade_maior = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        cont_feminino += 1
media = soma/cont_media
print(f'A média da idade do grupo é de {media:.2f} anos.'
      f'\nO homem mais velho dor grupo é do {nome_velho} que tem {idade_maior} anos.'
      f'\n{cont_feminino} mulheres tem menos de 20 anos')
