# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente
moldura = '=' * 30
lista_1 = []
lista_2 = []
print(moldura)
print('INSIRA AS NOTAS DOS ALUNOS')
print(moldura)
while True:
    lista_1.append(str(input('Nome do aluno: ')))
    for c in range(0, 2):
        lista_1.append(float(input(f'{c+1}ª nota: ')))
    lista_2.append(lista_1[:])
    lista_1.clear()
    pergunta = str(input('Quer continuar? (S/N): ')).strip().upper()
    while pergunta not in 'SN':
        if pergunta not in 'SN':
            print('Essa resposta é invalida.')
            pergunta = str(input('Quer continuar? (S/N): ')).strip().upper()
    if pergunta == 'N':
        break
print(moldura)
print('BOLETIM')
print(moldura)
print(f'{"No.": <5}{"NOME": <15}{"MEDIA": <3}')
print('_' * 30)
for i, v in enumerate(lista_2):
    print(f'{i: <5}{v[0]: <15}{(v[1]+v[2])/2: <3}')
print('_' * 30)
print(moldura, 'NOTAS INDIVIDUAIS', moldura)
notas = int(input('Mostrar notas de qual aluno? (999 p/ interromper): '))
while True:
    if notas == 999:
        break
    if notas > (len(lista_2) - 1):
        print('Esse aluno não esta no boletim.')
        print('_' * 30)
        notas = int(input('Mostrar notas de qual aluno? (999 p/ interromper): '))
    else:
        print(f'Notas de {lista_2[notas][0]} são {lista_2[notas][1:]}')
        print('_' * 30)
        notas = int(input('Mostrar notas de qual aluno? (999 p/ interromper): '))
print(moldura)
print('Ate breve.')

# Resolução do professor

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? (S/N): '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<<<< VOLTE SEMPRE >>>>>>>>>')
