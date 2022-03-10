# Refaça o Desafio 009, mostrando a tabuada de um numero que o usuário
# escolher, só que agora utilizando um laço for.

n = int(input('Digite o numero da tabuada de deseja: '))
print(5 * '=', f'Tabuada do {n}', 5 * '=')
for c in range(0, 11):
    # m = n * c teste sem usar variavel
    print(f'{n} x {c:2} = {n * c}')  # no format de c :2 retorna que o número deve ter 2 digitos
