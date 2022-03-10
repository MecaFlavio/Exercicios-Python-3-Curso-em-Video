# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo desconsiderando os
# espaços

frase = str(input('Frase: ')).strip().upper()  # Eliminei os espaços e deixei tudo maiuscula para comparação
palavras = frase.split()  # Separei as palavras em coleção

# juntei as palavras. O metodo .join juntas as coleçoes com o caractere antes do metodo, no caso nenhum espaço.
frase_2 = ''.join(palavras)
inverso = ''  # criei uma variavel sem caracteres dentro, para informar que é uma variavel tipo STR
for letra in range(len(frase_2) - 1, -1, -1 ):  # Contagem inversa no tamanho len da frase sem espaços
    inverso += frase_2[letra]  # Concatenando os caracteres inversamente
if inverso == frase_2:
    print(f'{frase_2} é um Palindromo')
else:
    print(f'{frase_2} não é um Palindromo')

# a = 'i' + 'o'  # é possivel concatenar caracteres
# print(a)