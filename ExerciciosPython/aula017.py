# Listas
tupla = (2, 5, 9, 1)
# não é possivel adicionar elementos numa tupla na execução do programa
# num[2] = 3
print(tupla)
# criando uma lista
lista = [2, 5, 9, 1]
print(lista)
# Adiciona elemento ao final da lista
lista.append(7)
print(lista)
# Ordena uma lista em ordem numérica e alfabética
lista.sort()
print(lista)
# Realiza a ordenação de maneira decrescente
lista.sort(reverse=True)
print(lista)
# Retorna os elementos da lista
print(len(lista))
# insere elementos na lista no indice que desejar, refaz as posições dos indices posteriores
lista.insert(2, 0)
print(lista)
# .pop() sem parametros emove o último valor da lista
lista.pop()
print(lista)
# .pop() retira da lista o elemento no indice do parametro
lista.pop(2)  # elemento no indice 2 é o 0
print(lista)
# inserção para testar metodo remove
lista.insert(2, 2)
print(lista)
# .remove retira apenas o primeiro resultado na lista igual ao elemento no argumento
lista.remove(2)
print(lista)
# posso executar laços para retirar valores
# lista.remove(4)  # dessa forma o python retorna um erro
if 2 in lista:
    lista.remove(2)
else:
    print("Esse valor não esta na lista")
print(lista)

lista_2 = []  # posso iniciar uma lista vazia dessa forma ou list()
lista_2.append(5)
lista_2.append(9)
lista_2.append(4)
for c, v in enumerate(lista_2):  # enumarate retorna o indice e o calor no elemento em duas variaveis declaradas no for
    print(f'Na posição {c} encontrei o valor {v}...')
print('Fim')

# posso inserir valores com input na lista
for c in range(0, 5):
    lista_2.append(int(input('Digite um valor: ')))
print(lista_2)
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a  # dessa forma as listas estão ligadas, se eu mexer numa lista eu altero da mesma forma a duas
b[2] = 8  # inserindo valor apenas na lista b
print(f'lista a {a}')  # lista a também recebeu o valor
print(f'lista b {b}')

# dessa forma eu estou inserido todos os valores da lista a na lista b usando fatianmento
b = a[:]  # Sem criar ligação entre as listas
b[2] = 10
print(f'lista a {a}')
print(f'lista b {b}')

