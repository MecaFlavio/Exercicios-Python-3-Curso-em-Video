# Faça um program que leia um número qualquer e mostre o seu fatorial;
# 5! = 5x4x3x2x1 = 120
contador = fator = fatorial = int(input('Qual numero deseja realizar o fatorial: '))
while contador != 1:
   numero = fatorial
   fatorial = numero * (contador - 1)
   contador -= 1
print(f'O fatorial de {fator}! é {fatorial:,}')

# Resolução do professor

fatorial = int(input('Qual numero deseja realizar o fatorial: '))
fator = fatorial
for contador in range(fator, 1, -1):
    numero = fatorial
    fatorial = numero * (contador - 1)
print(f'O {fator}! é {fatorial}')
