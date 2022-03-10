#  Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#  valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
#  (desconsiderando o flag).

cont = soma = 0
num = int(input('Digite um numero [ 999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    # no final para verificar a FLAG do while e não entra na contagem
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Voce digitou {cont} numeros e a soma desses numeros é {soma:,}')
