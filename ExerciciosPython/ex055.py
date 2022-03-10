
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e qual foi o menor peso lidos.

maior_peso = float(0)
menor_peso = float(0)
for c in range(1, 6):
    peso = float(input(f'Digite um peso da {c}ª pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print(f'O maior peso é {maior_peso:.2f} e o menor peso é {menor_peso}.')
