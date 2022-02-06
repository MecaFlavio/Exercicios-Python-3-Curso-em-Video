# Condições parte 1

#nome = str(input('Qual é o seu nome? '))
#if nome == 'Flavio':
#    print('Que nome lindo voce tem!')
#else:
#    print('Seu nome é tão normal!')
#print(f'Bom dia {nome}!')
#
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digirte a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
#if m >= 6.0:                               #Condilção composta
#    print('Sua media foi boa Parabéns!')
#else:
#    print('Sua media foi ruim! Estude mais')
print('Parabéns' if m >= 6 else 'Estude Mais!') #Condição Simplificada
