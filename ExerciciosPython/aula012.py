# Estruturas Aninhadas

nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Flavio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print(f'Bom dia {nome}!')
