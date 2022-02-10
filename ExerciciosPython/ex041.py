# A concentração nacional de natação precisa de um programa que leia o
# ano de nascimento de um atléta e mostre sua categoria, de acordo com a idade:
#
#  - até 9 anos: Mirim
#  - Até 14 anos: Infantil
#  - Até 19 anos: Junior
#  - Até 30 anos: Sênior
#  - Acima: Master

import datetime

ano = int(input('Em em qual ano você nasceu: '))
ano_int = int(datetime.datetime.today().strftime('%Y'))
idade = ano_int - ano
if idade <= 9:
    print(f'Você possui {idade} anos. Sua categoria é a MÍRIM.')
elif 9 < idade <= 14:
    print(f'Você possui {idade} anos. A categoria é INFANTIL.')
elif 14 < idade <= 19:
    print(f'Você possui {idade} anos. A categoria é JUNOR.')
elif 19 < idade <=30  :
    print(f'Você possui {idade} anos. A sua categoria é SÊNIOR')
else:
    print(f'Sua idade é {idade} anos. Você está na categoria MASTER')
