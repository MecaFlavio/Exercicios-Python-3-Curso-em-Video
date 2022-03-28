# Faça um programa que leia nome e média de um aluno,
# guardando também a situação num dicionário. No final,
# mostre o conteúdo de estrutura na tela.

dicionário = {'nome': str(input('Nome: ')), 'media': float(input('Media de: '))}
if dicionário['media'] < 5:
    dicionário['situação'] = 'Reprovado'
elif dicionário['media'] < 7:
    dicionário['situação'] = 'Recuperação'
else:
    dicionário['situação'] = 'Aprovado'
print('-=' * 30)
for k, v in dicionário.items():
    print(f'{k}: {v}')


