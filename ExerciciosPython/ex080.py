# Crie um programa onde o usuario possa digitar cinco valores numericos e cadsatre-os em uma lista,
# ja na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):
    numero = int(input('Digite um numero: '))
    if c == 0 or numero > lista[-1]:  # também posso apontar lista[len(lista)-1]
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):  # Essa codigo vai verificar cada posição da lista se o número é menor.
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(f'Os valores de lista são {lista}')
