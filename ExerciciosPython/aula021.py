# Funçoes - parte 2
# - interactive help
# - docstrings
# - argumentos opcionais
# - escopo de variaveis
# - retornos de resultados

# Interactive Help
# No python console digitando help a funçlão help() do python sera ativada e exibira manuais das palavras chaves
# ou usando o comando no script
help(print)
# ou input metodo .__doc__ na função. É uma DOCSTRING
print(input.__doc__)

print()


# DOCSTRINGS
# Posso criar docstrings para funçoes criadas abrindo aspas duplas logo abaixo da linha do paramentro def.
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


contador(2, 10, 2)
help(contador)


# PARAMETROS OPCIONAIS
def somar(a, b=0, c=0):  # numeros seguidos de 0 ou de algum valor nos parametros são parametros opcionais
    s = a + b + c
    print(f'A soma é {s}')


somar(2, 2, 2)
somar(1, 1)
somar(1)


# ESCOPO DE VARIAVEIS
# Local onde uma variavel vai existir e o local onde não vai mais existir
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')  # n retornara valor pois é uma variavel de escopo global
    print(f'Na função teste, x vale {x}')  # x retorna valor é uma variavels declarada apenas na funçãom, escopo local


# programa principal
n = 2
print(f'No programa principal, n vale {n}')  # n é uma variavel de escopo global
teste()


# print(f'No programa principal, x vale {x}')  # x nesse caso é uma varialvel de escopo local, nesse caso dara erro


# No python é possivel decalrar a variaveis de mesmo nome com escopos diferentes
def função():
    n1 = 4
    print(f'N1 local vale {n1}')


n1 = 2
função()
print(f'N1 global vale {n1}')


# Se na função eu declarar a variavel como global a varievel
# a ser manipulada sera a mesma declarada fora da função
def função2():
    global n1
    n1 = 4
    print(f'N1 local vale {n1}, foi declarada global')


n1 = 2
print(f'Antes da função n1 global vale {n1}')
função2()
print(f'N1 global vale {n1}, foi modificada dentro da função')


# RETORNO DE VALORES
# Para a função retornar um valor posso usar o metodo return
def soma2(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma2(2, 2, 5)
r2 = soma2(3, 2)
r3 = soma2(7)
print(f'Os resultados foram {r1}, {r2}, {r3}')


# EXERCICIO PRÁTICO
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')


def par(val=0):
    if val % 2 == 0:
        return True
    else:
        return False


num = int(input('Numero: '))
if par(num):
    print('É par')
else:
    print('Não é par')
