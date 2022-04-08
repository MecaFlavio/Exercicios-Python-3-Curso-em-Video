def leiaDinheiro(msg):
    valido = False
    while not valido:
        preço = str(input(msg)).replace(',', '.').strip()
        if preço.isalpha() or preço == '':
            print(f'\33[0;31mERRO. \"{preço}\" não é um valor valido.\033[m')
        else:
            valido = True
            return float(preço)

