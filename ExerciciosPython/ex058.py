# Melhora o jogo do Desafio 028 onde o computador vai 'Pensar' num número entre 0 e 10. Agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer
import random as rand

computador = rand.randint(0, 10)
resposta = 11  # Gambiarra ;)
palpites = 0
while resposta != computador:
    resposta = int(input('Advinhe o número entre 0 e 10: '))
    if resposta != computador:
        palpites += 1
        if resposta > computador:
            print('É um número menor! Tente novamente!')
        elif resposta < computador:
            print('É um número maior! Tente novamente!')
if resposta == computador:
    palpites += 1
    print(f'A sua resposta está correta, o número que pensei foi {computador}.'
          f'\nE voce tentou {palpites} vezes! Até logo!')

# Resolução do professor
computador = rand.randint(0, 10)
resposta = False  # BOA PRATICA :)
palpites = 0
while resposta != True:
    jogador = int(input('Advinhe o número entre 0 e 10: '))
    palpites += 1
    if jogador != computador:
        if jogador > computador:
            print('É um número menor! Tente novamente!')
        elif jogador < computador:
            print('É um número maior! Tente novamente!')
    if jogador == computador:
        resposta = True
print(f'A sua resposta está correta, o número que pensei foi {computador}.'
      f'\nE voce tentou {palpites} vezes! Até logo!')
