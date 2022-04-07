# Crie um programa que tenha uma função fatorial() que receba dois parametros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
# do fatorial.


def fatorial(n, show=False):
    """
    farotial() Calcula o fatorial de um número
    :param n: numero a ser calculado o fatorial
    :param show: (opcional) True para mostrar o calculo
    :return: numero do fatorial
    """
    contador = n
    while contador != 1:
        numero_local = n
        n = numero_local * (contador - 1)
        contador -= 1
    if show:
        for v in range(numero, 0, -1):
            if v == 1:
                print(f'{v}= {numero_local}')
            else:
                print(f'{v}x', end='')
    return f'O fatorial de {numero} é {numero_local}'


# programa principal
numero = int(input('Qual numero deseja ver o fatorial: '))
while True:
    opção = str(input('Deseja ver o processo de calculo? (S/N): ')).strip().upper()
    if opção not in 'SN':
        print('Essa opção não existe.')
    else:
        if opção in 'S':
            fatorial(numero, show=True)
            break
        elif opção in 'N':
            fatorial(numero)
            break
print(fatorial(numero))
print()
help(fatorial)


# Resolução do professor
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: Valor ser calculado
    :param show: (opcional) MOstrar o calculo
    :return: Valor do fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
