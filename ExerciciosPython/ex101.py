# Crie um programa que tenha uma função chamada voto() que
# vai receber como parametro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleiçoes


def voto(ano_nasci):
    # Escopo de importação, nesse caos o import esta local, economizando memoria na execução do programa
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasci
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 < idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


# programa pricipal
nascimento = int(input('Ano de nascimento (YYYY): '))
print(voto(nascimento))
