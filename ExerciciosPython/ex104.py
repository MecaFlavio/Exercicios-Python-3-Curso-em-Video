# Crie um programa que tenha a função leiaint()
# que vai duncionar de forma semelhante à função input do python,
# contudo fazendo a validação para aceitar apeas um valor numerico.
def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('Erro. Digite um numero inteiro')
    return valor


# programa pricipal
n = leiaint('Digite um numero: ')
print(f'O numero digitado foi {n}')


# resolução do professor
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero valido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Voce digitou o numero {n}')

def leiaInt(frase):
    print("-" * 30)
    while True:
        numInt = str(input(frase))

        if numInt.isnumeric():
            return numInt  # Return encerra o while
        else:
            print("\033[31mERRO! Digite um número inteiro!\033[m")


# Programa principal
n = leiaInt("Digite um número: ")
print(f"\nVocê digitou o número {n}")
