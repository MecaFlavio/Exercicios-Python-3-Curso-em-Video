# Crie um programa onde o usúario digite uma expressão qualquer que use parenteses. O aplicativo
# deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta
expre = str(input('Digite a expressão matemática: '))
lista = []
for simb in expre:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão esta correta')
else:
    print('A expressão está incorreta')
