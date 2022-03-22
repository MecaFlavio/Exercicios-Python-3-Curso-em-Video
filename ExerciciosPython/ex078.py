# Faça um program que leia 5 valores numericos e guarde numa lista
# No final mostre o maior, o menor e os seus respectivos lugares na lista

lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(f'O maior numero digitado foi {max(lista)} que está na posição ', end="")
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end="")
print()
print(f'O menor número digitado foi {min(lista)} que está na posição ', end="")
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end="")
print()
