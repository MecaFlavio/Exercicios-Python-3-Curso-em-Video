# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#n = int(input('Digite um numero de 0 a 9999: '))
#n = str(n).strip()
#print(f'A unidade é {n[3]},'
#      f'\nA dezena é {n[2]},'
#      f'\nA centena é {n[1]}'
#      f'\nA milhar é {n[0]}.')

# Resoloção do professor

n = int(input('Digite um numero de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'A unidade é {u},'
      f'\nA dezena é {d},'
      f'\nA centena é {c},'
      f'\nA milhar é {m}.')
a = 1234//100
print(a)
b = a % 10
print(b)

