# Crie um programa que tenha uma tupla totalmente preenchida por extenso, de zero até vinte
# O programa deveré ler um número pelo teclado (entre 0 e 20) e mostra-lá por extenso

numeral = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desesete',
           'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    while numero < 0 or numero > 20:
        print('Este numero não está entre 0 e 20. Tente novamente.')
        numero = int(input('Digite um núemro entre 0 e 20: '))

    print(f'O número digitado foi {numeral[numero]}.')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? (S/N): ')).strip().upper()
        if resposta not in 'SN':
            print('Essa resposta esta incorreta.')
    if resposta == 'N':
        break


