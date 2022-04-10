def leiaInt(msg):
    while True:
        try:
            nint = int(input(msg))
            return nint  # O return pode ser colocado antes do final da função e para a execução da função
        except (ValueError, TypeError):  # é interessante tratar erro a erro no codigo
            print('\033[1;101mERRO. Digite uma opção válida!\033[m')
            continue  # continue continua o loop infinito
        except (KeyboardInterrupt):
            print('\033[1;101mAtenção! O usuário escolheu não digitar nenhum valor!\033[m')
            return 3


def linha(tam=42):
    return '_' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc