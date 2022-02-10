# Faça um programa que leia o ano de nascimento de um jovem e informe, de
# acordo com sua idade:
#
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou o tempo do alistamento.

from datetime import datetime # modulo que importa data do sistema

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual_str = datetime.today().strftime('%Y')# metodo strftime() formata a data de int para string
ano_atual_int = int(ano_atual_str)# Convertendo o ano de string para int

if ano_atual_int - ano_nasc == 18:
    print('Este ano voce estará com 18, você precisa se alistar!')
elif ano_atual_int - ano_nasc < 18:
    print('Voce ainda vai fazer 18 anos, voce ainda não precisa se alistar')
else:
    print('Voce ja passou da idade de se alistar')
