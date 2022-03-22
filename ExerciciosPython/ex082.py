# Crie um programa que vai ler vários numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas o valores pares
# e os valores impares digitados
# Ao final, mostre o conteúdo das três listas geradas
lista = list()
lista_par = list()
lista_impar = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    resposta = str(input('Quer continar?: (S/N) ')).strip().upper()
    while resposta not in 'SN':
        print('Essa reposta está incorreta.')
        resposta = str(input('Quer continuar?: (S/N) ')).strip().upper()
    if resposta == 'N':
        break
for v in range(0, len(lista)):
    if lista[v] % 2 == 1:
        lista_impar.append(lista[v])
    else:
        lista_par.append(lista[v])
print(f'Os numeros digitados foram {lista},'
      f'\nOs números pares são {lista_par},'
      f'\nOs Números impares são {lista_impar}')
