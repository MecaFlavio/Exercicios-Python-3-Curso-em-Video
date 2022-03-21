# Crie um programa onde o usuario possa digitar cinco valores numericos e cadsatre-os em uma lista,
# ja na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for v in range(0, 5):
    numero = int(input('Digite um numero: '))
    if numero >= lista[v]:
        lista.insert(v, numero)
    if numero <= lista[v]:
        lista.insert(v, numero)
print(lista)
