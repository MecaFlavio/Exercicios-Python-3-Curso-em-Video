#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome da cidade em que nasceu: ')).strip()
c = cidade.lower()
print(c.count('santo') == 1) # Verifica a quantidade de 'santo' aparece na frase. função errada para o exercicio.

# Resolução do professor

cid = str(input('digite a cidade em que nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO') # Verifica se a palavra 'SANTO' aparece no começo da frase.