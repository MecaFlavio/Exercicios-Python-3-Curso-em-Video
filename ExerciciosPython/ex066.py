# Crie um programa que leia varios números inteiros pelo teclado. O programa só vai
# parar quando o usuário digtar o valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)

print(20 * '=', '\n  Somando Números')
print(20 * '=')
soma = cont = 0
while True:
    número = int(input('Digite um numero: '))
    if número == 999:
        break
    cont += 1
    soma += número
print(20 * '=', f'\nVocê digitou {cont} numeros e a soma dos numeros é de {soma}')






