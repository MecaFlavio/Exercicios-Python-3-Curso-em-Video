# Faça um programa que tenha uma função chamada escreva(),
# que receba um texo qualquer como parametro e mostre uma
# mensagem com tamnho adaptável.

def escreva(txt):
    c = len(txt) + 4
    print('-' * c)
    print(f'{txt:^{c}}')
    print('-' * c)


frase = str(input('Frase: '))
escreva(frase)

