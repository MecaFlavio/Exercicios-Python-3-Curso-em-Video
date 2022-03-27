##Leia um numero inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Insira um numero para saber sua tabuada: '))
a = n * 0
b = n * 1
c = n * 2
d = n * 3
e = n * 4
f = n * 5
g = n * 6
h = n * 7
i = n * 8
j = n * 9
k = n * 10

print(f'A tabuada do {n} é:'
      f'\n9x0={a}'
      f'\n9x1={b}'
      f'\n9x2={c}'
      f'\n9x3={d}'
      f'\n9x4={e}'
      f'\n9x5={f}'
      f'\n9x6={g}'
      f'\n9x7={h}'
      f'\n9x8={i}'
      f'\n9x9={j}'
      f'\n9x10={k}')
# outra forma
print('='*12)
print(f'{n} x {1:2} = {n*1}')
print(f'{n} x {2:2} = {n*2}')
print(f'{n} x {3:2} = {n*3}')
print(f'{n} x {4:2} = {n*4}')
print(f'{n} x {5:2} = {n*5}')
print(f'{n} x {6:2} = {n*6}')
print(f'{n} x {7:2} = {n*7}')
print(f'{n} x {8:2} = {n*8}')
print(f'{n} x {9:2} = {n*9}')
print(f'{n} x {10:2} = {n*10}')
print('='*12)