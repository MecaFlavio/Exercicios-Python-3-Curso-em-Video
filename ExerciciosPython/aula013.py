# Aula de estrutura de repetição com variavel de controle

for c in range(0, 6):
    print('oi')
print('fim')

for a in range(0, 10, 2):  # o primeiro argumento e o segundo é o range de contagem, o terceiro é o metodo da contagem
    print(a)
print('fim')
# Outro exemplo
for a in range(10, 0, -1):  # Com uma condição de contagem regressiva
    print(a)
print('Fim')
# Utilizando input
n = int(input('Numero: '))
for c in range(0, n+1):
    print(c)
print('fim')

s = 0
for c in range (0, 4):
    n = int(input('Digite um numero'))
    s += n  # Esta sintaxe s += n significa s = s + n, python permite esse tipo de apontamento
print(s)
