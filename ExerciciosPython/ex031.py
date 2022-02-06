# Desenvolva um programa que pergunta a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por viagens de até 200km/h e cobrando R$ 0,45 pra viagens mais longas.

distancia = int(input('Qual a distancia da viagem: '))
if distancia <= 200:
    print('Será cobrado R$0,50 por km rodado. A sua viagem vai custar R${:.2f}'.format(distancia * 0.5))
else:
    print(f'Sua viagem vai custar R${distancia * 0.45}. Com desconto para viagens mais longas!')
