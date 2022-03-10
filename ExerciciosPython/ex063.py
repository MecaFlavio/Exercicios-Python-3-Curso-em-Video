# Sequencia de fibonacci

termo_1 = 0
termo_2 = 1
termos = int(input('Quantos termos da sequencia de fibonacci quer mostrar: '))
termo_3 = termo_1 + termo_2
c = 3  # Sequecia inicia do terceiro termo
if termos == 2:
    print(termo_1, termo_2)
elif termos == 1:
    print(termo_1)
elif termos > 2:
    while c <= termos:  # Sequecia inicia do terceiro termo
        print(termo_3, end=' ')
        # Lógica de fibonacci criada onde o resultado se soma ao termo anterior
        termo_1 = termo_2
        termo_2 = termo_3
        termo_3 = termo_1 + termo_2
        c = c + 1

else:
    print('Até logo')
print('FIM')
