# Aprimore o desafio anterior, mostrando:
# a) A soma de todos os valores pares digitados
# b) A soma dos valores da terceira coluna
# c) O Maior valor da segunda linha

soma_par = soma_coluna = cont = maior = 0
matriz = [[], [], []]
for v in range(0, 3):
    for c in range(0, 3):
        matriz[v].append(int(input(f'Digite um valor para [{v},{c}]: ')))
        if matriz[v][c] % 2 == 0:
            soma_par += matriz[v][c]
        if c == 2:
            soma_coluna += matriz[v][c]
        if v == 1:
            if cont == 0 or matriz[v][c] > maior:
                maior = matriz[v][c]
                cont += 1
for v in range(0, 3):
    for c in range(0, 3):
        print(f' {matriz[v][c]: ^5}]', end='')
    print()
print(f'A soma da 3ª coluna é {soma_coluna}')
print(f'A soma dos numeros pares é {soma_par}')
print(f'O maior número da segunda linha é {maior}')
