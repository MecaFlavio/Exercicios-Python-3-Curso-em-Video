# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).strip().lower()
a = frase.count('a')
b = frase.find('a')
c = frase.rfind('a')
print(a, b + 1, c + 1) # Codigo corrigido

# Resolução do Professor

frase = str(input('Escreva uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira vez que que a letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima vez que a letra A aparece é na posição {}'.format(frase.rfind('A')+1))

