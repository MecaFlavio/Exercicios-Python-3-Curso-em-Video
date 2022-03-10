# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu Sexo (M / F): ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Não identifiquei seu sexo, tente novamente!')
if sexo == 'F':
    sexo = 'Feminino'
elif sexo == 'M':
    sexo = 'Masculino'
print('Seu sexo é {}'.format(sexo))
