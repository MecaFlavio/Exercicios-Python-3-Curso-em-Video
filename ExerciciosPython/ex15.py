# Escreva um programa que leia a quantidade de  KM percorridos por um carro
# Alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
# pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.

d = float(60.00)
r = float(0.15)
dias = int(input('Quantos dias de aluguel: '))
km = float(input('Quantos Km rodados: '))
valor = float((d * dias) + (km * r))
print(f'O total a pagar é de R${valor:.2f}')
