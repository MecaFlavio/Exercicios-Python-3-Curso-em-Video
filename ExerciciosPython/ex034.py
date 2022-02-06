#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
#  superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o Salario do funcionario: '))
if salario > 1250.00:
    reajuste_salario = salario * 1.1
    print(f'Esse salario recebe 10% de aumento e passa a ser R${reajuste_salario:.2f}')
else:
    reajuste_salario = salario * 1.15
    print(f'Agora esse salario recebe 15% de aumento e passa a ser R${reajuste_salario:.2f}')
