# 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa devera perguntar se o usuário quer ou não continuar. No final, mostre:
#
# a) quantas pessoas tem mais de 18 anos.
# b) quantos homens foram cadastrados.
# c) quantas mulheres tem menos de 20 anos

# Minha solução

cont_idade_18 = 0
cont_sexo_masc = 0
cont_fem_20 = 0
while True:
   sexo = str(input('Qual o seu sexo (M / F): ')).strip().upper()
   if sexo in 'MF':
       idade = int(input('Qual a sua idade: '))
       if idade > 0:
           if sexo == 'M':
               cont_sexo_masc += 1
           if sexo == 'F' and idade < 20:
               cont_fem_20 += 1
           if idade > 18:
               cont_idade_18 += 1
           resposta = ' '
           while resposta not in 'SN':
                resposta = str(input('Quer continuar? (S/N): ')).strip().upper()
           if resposta == 'N':
               break
       else:
           print('Esta informação está incorreta, tente novamente.')
   else:
       print('Essa informação está incorreta, tente novamente.')
print(f'''{cont_idade_18} tem mais de 18 anos.
{cont_sexo_masc} homens foram cadastrados.
{cont_fem_20} mulheres tem menos de 20 anos''')

# Resolução do professor

# tot_18 = tot_h = tot_M_20 = 0
# while True:
#    idade = int(input('Idade: '))
#    sexo = ' '  # fica dentro do while infinito para receber valos vazio sempre
#    while sexo not in 'MF':
#        sexo = str(input('Sexo: (M/F): ')).strip().upper()
#    if idade >= 18:
#        tot_18 += 1
#    if sexo == 'M':
#        tot_h += 1
#    if sexo == 'F' and idade < 20:
#        tot_M_20 += 1
#    resp = ' '
#    while resp not in 'SN':
#        resp = str(input('Quer continuar? (S/N): ')).strip().upper()
#    if resp == 'N':
#        break
# print(f'Total de pessoas com mais de 18 anos: {tot_18}')
# print(f'Ao todo temos {tot_h} homens cadastrados')
# print(f'E temos {tot_M_20} mulheres com menos de 20 anos')
