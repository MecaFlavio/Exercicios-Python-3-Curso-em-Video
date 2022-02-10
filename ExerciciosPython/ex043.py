# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo:
#
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Morbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'IMC {imc:.1f}. Voce está a baixo do peso ideal.')
elif 18.5 <= imc <= 25:
    print(f'IMC {imc:.1f}. Você está no peso Ideal')
elif 25 < imc <= 30:
    print(f'IMC {imc:.1f}. Você está com Sobre Peso.')
elif 30 < imc <= 40:
    print(f'IMC {imc:.1f}. Você está com Obesidade.')
elif 40 < imc:
    print(f'IMC {imc:.1f}. Você está com Obesidade Morbida.')
