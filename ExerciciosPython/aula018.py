# Variaveis compostas — Lista parte 2
teste = list()
teste.append('Flavio')
teste.append(32)
print(teste)
galera = list()
# inserir uma lista dentro de outra lista requer o uso de [:] para não ligar listas
galera.append(teste[:])  # cria uma cópia da lista sem dependencia
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera, teste)

# posso criar listas dessa forma também
galera_2 = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera_2[2][0])  # forma de fatiamento de listas

# Exemplos de aplicações

for p in galera_2:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera_3 = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera_3.append(dados[:])
    dados.clear()
print(galera_3)

tot_maior = tot_menor = 0
for p in galera_3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        tot_maior +=1
    else:
        print(f'{p[0]} não é maior de idade')
        tot_menor += 1
print(f'{tot_maior} pessoas são maiores de idade e {tot_menor} não são maiores de idade')

