# Faça um programa que calcula a soma entre todos os números impares
# que são multiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
for c in range(1, 501, 1):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c  # posso escrever soma += c, tem a mesma finalidade
print(soma)
