# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostra uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite

import random

print('Lendo sua velocidade....')

v = random.randrange(40, 161)
if v > 80:
    m = (v - 80) * 7
    print('Sua velocidade é {}km/h. Você foi multado de deve pagar R${:.2f}. '
          '\nDirija mais devagar da proxima vez!'.format(v, m))
else:
    print('Sua velocidade foi {}Km/h. Você está dentro do limite de velocidade.'.format(v))
