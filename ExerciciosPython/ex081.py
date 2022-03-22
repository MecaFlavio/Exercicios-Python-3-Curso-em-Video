# Crie um programa que vai ler vários números e colocar numa lista.
# a) Quantos números foram digitados
# b) A lista de valores ordenada de forma decrescente
# c) Se o valor 5 foi digítado e está ou não na lista
cont = 0
lista = list()
while True:
    lista.append(int(input('Insira um Número: ')))
    resposta = str(input('Deseja inserir outro numero? (S/N): ')).strip().upper()
    while resposta not in 'SN':
        if resposta not in 'SN':
            print('Essa reposta não é valida. Digite (S) ou (N).')
            resposta = str(input('Deseja inserir outro numero? (S/N): ')).strip().upper()
    if resposta == 'N':
        break
print(f'A lista de numeros digitados foi {len(lista)} números',)
lista.sort(reverse=True)
print(f'Os numeros da lista em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O número 5 está na lista e aparece {lista.count(5)} vez(es) ')
else:
    print('O número 5 não foi digitado nenhuma vez')
