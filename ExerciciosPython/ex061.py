# Refaça o desafio 051, lendo o primeiro termo e a razão da uma PA, mostrando os 10 primeiros termos da PA
# usando a estrutura while

termo_1 = int(input('Digite o primero termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
while cont <= 10:
    pa = termo_1 + ((cont - 1) * razao)
    cont += 1
    print(pa, end=" ")

# Resolução do professor

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end="")
    termo += razão
    cont += 1
print('FIM')
