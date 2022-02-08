# Escreva um programa que leia um numero inteiro e peça para o usuario escolher
# qual será a base de conversão
#
# 1- para binario
# 2- para octal
# 3- para hexadecimal

n = int(input('Digite um número Decimal inteiro: '))
print('Opções:'
      '\n1 - Binario'
      '\n2 - Octal'
      '\n3 - Hexadecimal')
base_conversao = int(input('Qual opção deseja: '))
if base_conversao == 1:
    binario = bin(n)[2:]
    print(binario)
elif base_conversao == 2:
    octal = oct(n)[2:]
    print(octal)
elif base_conversao == 3:
    hexadecimal = hex(n)[2:]
    print(hexadecimal)
else:
    print('Essa opção não existe.')

# Resolução do Professor

#num = int(input('Digite um numero inteiro: '))
#print('''Escolha uma das bases para conversão:
#[ 1 ] Converter para Binario
#[ 2 ] Converter para Octal
#[ 3 ] Converter para Hexadecimal''')
#opção =int(input('Sua opção: '))
#if opção == 1:
#    print('{} em binario é igual a {}'.format(num, bin(num)[2:]))
#elif opção == 2:
#    print('{} em octal é igual a {}'.format(num, octal(num)[2:]))
#elif opção == 3:
#    print('{} em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
#else:
#    print('Essa opção não existe')