##Leia um valor em metros e converta em centimentros e milimetros
m = float(input('Insira uma medida em metros: '))
c = m * 100
mm = m * 1000
print(f'{m:.2f} metros equivale a {c:.2f} centimetros e a {mm:.2f} milimetros')
