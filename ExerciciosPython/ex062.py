# Melhore o desafio 061, perguntando par o usuario se ele quer mostrar mais alguns termos. O programa escerra quando ele
# que quer mostrar 0 termos

# Recebe o primeiro termo
termo_1 = int(input('Digite o primero termo da PA: '))

# Recebe a Razão
razao = int(input('Digite a razão da PA: '))

# Contador de repetiçoes, ao final tera sempre um número a mais do total de termos
cont = 1

# Total de termos
total = 0

# Variavel para receber continuação da PA, inicia com os 10 primeiros termos
# somara ao total, se receber o valor 0 encerra o programa.
continua_pa = 10

while continua_pa != 0:
    total += continua_pa  # total termina com 10 na primeira run
    while cont <= total:
        pa = termo_1 + ((cont - 1) * razao)  # Formula da PA
        print(pa, end=" ")  # Exibe a cada termo da PA
        cont += 1  # Contador termina com valo 11 na primeira run
    print('')  # apenas para pular linha apos a execução do while
    continua_pa = int(input('Quer continuar com quantos termos: '))  # soma o valor inserido ao total da primeira run
print(f'Foram exibidos {total} termos na PA de {termo_1} com razão {razao}.')

# Resolução do professor

#print('Gerador de PA')
#print('-=' * 10)
#primeiro = int(input('Primeiro Termo: '))
#razão = int(input('Razão da PA: '))
#termo = primeiro
#cont = 1
#total = 0
#continua_pa = 10
#while continua_pa != 0:
#    total = total + continua_pa
#    while cont <= total:
#        print('{} → '.format(termo), end="")
#        termo += razão
#        cont += 1
#    print('PAUSA')
#    print(total, termo, cont)
#    continua_pa = int(input('Quantos termos você quer mostrar a mais? '))
#print('Progressão finalizada com {} termos mostrados.'.format(total))
