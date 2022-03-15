# Aula 15 - Intenrrompendo repetições

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break  # para o laço a no momento que colocar, nessa caso testa o 999, mas não soma.
    s+= n
print(f'A soma é {s}.')