# Aula 16 - Vaiaveis compostas: Tuplas


lanche = ('hamburger', 'suco', 'pizza', 'pudim')  # tupla criada, pode ser criada sem parenteses np python 3
print(lanche)  # mostra a tupla em parenteses e os seus elementos
print(lanche[1])  # mostra o elemento 1 da tupla
print(lanche[-1])  # mostra o elemento -1 da tupla
# Tuplas recebem indices numericos crescentes e decrescentes ex: 0,1,2 e -1,-2,-3 respectivamente
print(lanche[3])  # mostra o elemento 3 da tupla
print(lanche[-2])  # mostra o elemento - 2 da tupla
print(lanche[1:3])  # imprime do elemento 1 ao elemento 2 desconsiderando o elemento 3
print(lanche[2:])  # imprime o elemento 2 até o ultimo
print(lanche[:2])  # imprime do início até o elemento 1 ignorando o elemento 2
print(lanche[-2:])  # imprime do -2 até o final, pizza até pudim
print(lanche[3:-5:-1])  # imprime do elemento 3 ao 0 em ordem decrescente
## lanche[1] = refrigerante  # retorna erro, tuplas são imutáveis durante a execução do programa.
print(lanche)

# Percorre o for para cada elemento indexado da Tupla
for comida in lanche:
    print(f'Eu vou comer {comida};')
print('Comi pra caramba')

print(len(lanche))  # mostra a quantidade de elementos da tupla
# O range vai de 0 à quantidade de elementos da tupla lanche = (4)
# Por tanto mostra o indice correspondentes de 0 a 3
for cont1 in range(0, 4):  # pode ser lido, 'mostre 4 resultados iniciando do 0. 0,1,2,3 = 4 resultados
    print(cont1)

for cont in range(0, len(lanche)):
    print(lanche[cont])

for cont2 in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont2]} na posição {cont2}')

# Metodo enumerate retorna uma tupla para cada elemento na tupla lanche
# no primeiro indice ele aloca o número no segundo indice aloca o elemento
# após o for aponto duas variaveis se quiser guadar separadamente
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# O metoto sorted cria lista com a tupla e organiza em ordem alfabetica
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
# soma de tuplas realiza a comutação de elementos, ou seja, apenas junta os elementos numa terceira tupla
print(c)
# Nesse caso, por tanto, a + b não sera igual b + a.. A ordem da soma influencia em como os elementos serão indexados
c = b + a
print(c)

print(len(c))  # imprime o número de elementos de c
print(c)

print(c.count(5))  # mosta a quantidade de elementos 5 que a tupla possui
print(c.count(4))  # mostra a quantidade de elementos 4 na tupla
print(c.count(9))  # mostra que não possui o elemento
print(c.index(8))  # mostra o indice do elemento
print(c.index(4))  # mostra o indice do elemento
print(c.index(5))  # mostra o indice do elemento, na caso do primeiro encontrado
print(c.index(5, 1))  # mostra o indice do elemento a partir do indice 1

# Uma tupla pode receber elementos de tipos diferentes
pessoa = ('Flavio', 32, 'Casado', 'peso', 110)
print(pessoa)

# É possivel deletar uma tupla durante a execução do programa com o comando del
## del lanche
print(lanche)
