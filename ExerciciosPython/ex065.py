# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

cont = numero = soma = media = maior = menor = 0
pergunta = 'S'
while pergunta != 'N':
    numero = int(input('Digite um numero: '))
    cont += 1
    soma += numero
    if cont == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    pergunta = str(input('Quer continuar [S / N]: ')).strip().upper()
if cont == 0:
    print('Até logo')
else:
    media = soma / cont
    print(f'Voce digitou {cont} numeros, a soma foi de {soma},'
      f'\na media dos numeros que digitou é {media:.2f}, '
      f'\no maior numero que digitou foi {maior} '
      f'\ne o menor numero foi {menor}')

# Resolução do professor

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número> '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar: [S/N]: ')).upper().strip()[0]
media = soma/quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
