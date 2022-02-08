# Escreva um programa para aprovar o emprestimo bancario para a compra de
# uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador
# e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ele não pode exceder 30%
# do salário ou então o empréstimo será negado.

print(5*'=', 'SEU EMPRESTIMO SERÁ ANALISADO',5*'=')
valor = float(input('Qual o valor do imovel: '
                '\n'))
salario = float(input('Qual o seu salario Bruto:'
                '\n'))
periodo = int(input('Em quantos anos pretende pagar: '
                    '\n'))
pagamento_mensal = valor/(periodo*12)
print('Analisando...')
if pagamento_mensal > (0.3*salario):
    print(f'Seu emprestimo foi negado. O valor da prestação é de R${pagamento_mensal:.2f}'
          f'\ne excede o valor de 30% do seu salário')
else:
    print(f'O empréstimo foi aprovado!! O valor da prestação é de R${pagamento_mensal:.2f}')
