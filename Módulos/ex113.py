# Reescreva a função do desafio 104, incluindo agora a possibilidade
# da digitação de um numero de tipo invalido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            nint = int(input(msg))
            return nint  # O return pode ser colocado antes do final da função e para a execução da função
        except (ValueError, TypeError):  # é interessante tratar erro a erro no codigo
            print('\033[1;101mERRO. Digite um valor Inteiro válido!\033[m')
            continue  # continue continua o loop infinito
        except (KeyboardInterrupt):
            print('\033[1;101mAtenção! O usuário escolheu não digitar nenhum valor!\033[m')
            return 0


def leiaFloat(msg):
    while True:
        try:
            nfloat = float(input(msg))
            return nfloat
        except (ValueError, TypeError):
            print('Erro! Digite um valor Real válido.')
            continue
        except (KeyboardInterrupt):
            print('\033[1;101mAtenção! O usuário escolheu não digitar valores\033[m')
            return 0


# programa pricipal
r = leiaInt('Digite um numero Inteiro: ')
f = leiaFloat('Digite um número Real: ')
print(f'O numero inteiro digitado foi {r} e o valor Real foi {f}')
