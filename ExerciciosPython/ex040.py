# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com sua média atingida:
#
#  - Media abaixo de 5.0: Reprovado
#  - Media entre 5.0 e 6.9: Recuperação
#  - Media 7.0 ou superior: Aprovado

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

média = (nota_1 + nota_2)/2

if média < 5:
    print('Sua Média foi {:.1f}. Você está reprovado.'.format(média))
elif 5 <= média < 7:
    print('Sua média foi {:.1f}. Você está de recuperação.'.format(média))
else:
    print('Sua média foi {:.1f}. Você está aprovado.'.format(média))

