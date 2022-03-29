# Faça um programa que leia o ano de nascimento de um jovem e informe, de
# acordo com sua idade:
#
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou o tempo do alistamento.

from datetime import datetime  # modulo que importa data do sistema

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual_str = datetime.today().strftime('%Y')  # metodo strftime() formata a data de int para string
ano_atual_int = int(ano_atual_str)  # Convertendo o ano de string para int

if ano_atual_int - ano_nasc == 18:
    print('Este ano voce estará com 18, você precisa se alistar!')
elif ano_atual_int - ano_nasc < 18:
    print('Voce ainda vai fazer 18 anos, voce ainda não precisa se alistar')
else:
    print('Voce ja passou da idade de se alistar')

# Resolução do Professor

from datetime import date

atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos  para alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))