## Leia um valor em metros e exiba convertido em milimetros
m = float(input('Insira uma medida em metros: '))
c = m * 100
print(f'{m:.2f} metros equivale a {c:.2f} centimetros'
      f'\nE equivale a {m*1000:.2f} milimetros')
