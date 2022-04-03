# Funções - parte 1

def lin():
    print('_' * 30)


# programa principal deve ter duas linhas de distância
lin()
print('Curso em Video')
lin()
print('Aprenda Python')
lin()


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# programa principal
titulo('Curso em video')
titulo('Aprenda Python')

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)


def soma(a, b):
    print(f'a = {a} e b  = {b}')
    s = a + b
    print(s)


# programa principal
soma(4, 5)
soma(8, 9)
soma(1, 2)
# soma(4) # A função recebe 2 parametros, esse comando dara erro

soma(b=2, a=5)  # posso mudar a ordem contanto que eu explicite

# empacotamento


# * no parametro significa que a variavel num vai receber varios valores e ira retornar numa tupla
def contador(* num):
    tam = len(num)
    print(num)
    for v in num:
        print(f'{v}; ', end='')
    print()
    print(f'Recebi o valores {num} e são ao todo {tam} numeros')


# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 2, 3, 8)


# trabalhando com listas e funçoes
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 6, 1, 5]
dobra(valores)
print(valores)


# desempacotamento
def adição(* val):
    s = 0
    for v in val:
        s += v
    print(f'A soma de {val} é {s}')


adição(5, 2)
adição(2, 9, 4)
