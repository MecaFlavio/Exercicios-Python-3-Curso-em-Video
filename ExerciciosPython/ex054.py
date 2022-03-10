# Crie um programa que leia o ano de nascimento de sete pessoas. No final
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
ano = int(datetime.datetime.today().strftime('%Y'))
count_1 = 0
count_2 = 0
for c in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = ano - nasc
    if idade >= 18:
        count_1 += 1
    else:
        count_2 += 1
print(f"{count_1} pessoas são maiores e {count_2} pessoas ainda são menores")
