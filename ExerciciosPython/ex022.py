# Leia um nome completo e mostre o nome com todas as letras maiusculas
# o nome com todas minusculas, quantas letras no total (sem considerar espaço) e
# quantas letras tem o primeiro nome.

t = str(input('Nome aqui: '))
print(f'Seu nome em maiusculas é {t.upper()}')
print(f'Seu nome em minusculas é {t.lower()}')
a = t.split()
print(f'O primeiro nome é {a[0]} e tem {len(a[0])} letras')

# Resolução do Professor

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' '))) #uma forma de contar o nome, total do nome
                                                                    # menos os espaços identificados pelo metodo .count
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print(nome.find(' ')) #volta o numero da lista onde a str esta indexada