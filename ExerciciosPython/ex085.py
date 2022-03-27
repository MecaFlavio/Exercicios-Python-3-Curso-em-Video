# Crie um programa onde o usuario possa digitar sete valores numéricos e cadastre-os numa lista unica
# que mantenha separados os valores pares e impares. No final, mostre os valores impares e pares em ordem crescente

numero = 0
lista = [[], []]  # forma de declarar lista dentro de uma lista
for v in range(0, 7):
    numero = int(input(f'Digite o {v + 1}º numero: '))
    if numero % 2 == 0:
        lista[0].append(numero)  # inserção de valor em lista composta
    else:
        lista[1].append(numero)  # inserção de vaslor em lista composta
lista[0].sort()
print(f'Os numeros pares são {lista[0]}')
lista[1].sort()
print(f'Os números impares são {lista[1]}')
