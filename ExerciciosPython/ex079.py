# Crie um programa onde o usuario posa digitar varios valores e cadastre-os em uma lista. Caso o número
# ja exista la dentro, ele não sera adicionado. No final, serão exibidos todos os valores unicos
# digitados, em ordem crescente.

lista = []
resposta = ' '
while True:
    lista.append(int(input('Digite um número: ')))
    numero_2 = lista.count(lista[len(lista)-1])
    if numero_2 > 1:
        lista.pop()
        print('Esse numero ja existe na lista. Não foi adicionado')
    resposta = str(input('Quer ontinuar: S/N: ')).strip().upper()
    while resposta not in 'SN':
        if resposta not in 'SN':
            print('Essa resposta não existe.')
            resposta = str(input('Quer continuar: S/N: ')).strip().upper()
    if resposta == 'N':
        break
lista.sort()
print(f'Os numeros digitados foram {lista}')
