# Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa dever conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols')


n = str(input('Nome do Jagdor: ')).strip()
g = str(input('Numero de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
