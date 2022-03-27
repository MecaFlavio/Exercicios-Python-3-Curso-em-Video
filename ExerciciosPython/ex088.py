# Faça um program que ajude um jogador da mega sena a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 numeros entre 60 e 1 para cada jogo, cadastrando
# tudo numa lista composta
import random
import time
numero = 0
jogos = []
lista_jogos = []
moldura = '-=' * 20
print(moldura)
print(f'{"JOGO DA MEGA SENA": ^40}')
print(moldura)
numjogos = int(input('Quantos jogos gostaria de fazer: '))
for v in range(0, numjogos):
    jogos.clear()
    while len(jogos) < 6:
        numero = random.randint(1, 60)
        if jogos.count(numero) < 1:
            jogos.append(numero)
    jogos.sort()
    lista_jogos.append(jogos[:])
print(moldura)
print('Os jogos da mega sena são:')
for i, v in enumerate(lista_jogos):
    print(f'O {i + 1}º jogo é {v}')
    time.sleep(1)
print(moldura)

