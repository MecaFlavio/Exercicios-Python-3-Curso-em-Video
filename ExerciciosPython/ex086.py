# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela com a formatação

matriz = [[], [], []]
for v in range(0, 3):
    for c in range(0, 3):
        matriz[v].append(int(input(f'Digite um valor para [{v},{c}]: ')))
for v in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[v][c]: ^5}]', end='')
    print()
