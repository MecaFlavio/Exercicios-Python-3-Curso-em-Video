# Faça um programa que faça a tabuada de varios numeros, um de cada vez, para cada valor
# digitado pelo usuário. Programa será interrompido quando o número soliciotado for
# negativo.

# passos
# cria logica da tabuada
# criar laço de repetição
# criar condição de parada
# formatar

while True:
    print(20 * '=', '\nGERADOR DE TABUADAS')
    print(20 * '=', '\n(Digite -1 para sair.)')
    numero = int(input('Qual tabuada deseja ver: '))
    if numero < 0:
        print(20 * '=', '\nObrigado, até logo')
        break
    else:
        for c in range(0, 11):
            resultado = numero * c
            print(f'{numero} x {c:2} = {resultado}')
