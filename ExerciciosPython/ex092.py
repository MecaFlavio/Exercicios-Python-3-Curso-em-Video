# Crie um programa que leia o nome, ano de nacscimento e carteira de trabalho e cadastre-os(com idade) num
# dicionário se por acaso a CTPS for diferente de zero, o dicionário recebrá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
dicionario['Idade'] = (date.today().year - int(input('Ano de Nascimento: ')))
dicionario['CTPS'] = int(input('Nº Carteira de Trabalho (0 p/ não possui): '))
if dicionario['CTPS'] > 0:
    dicionario['Contratação'] = int(input('Ano de contratação: '))
    dicionario['Aposentadoria'] = (35 - (date.today().year - dicionario['Contratação'])) + dicionario['Idade']
    if (35 - (date.today().year - dicionario['Contratação'])) <= 0:
        dicionario['Aposentadoria'] = 'Você ja pode se aposentar'
    dicionario['Salario'] = float(input('Salário: '))
print('-=' * 30)
for k, v in dicionario.items():
    print(f'{k}: {v}')