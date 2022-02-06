a = input('Digite algo: ')
print('O tipo primitivo do que voce digitou é:',type(a))
print('Só tem espaços?', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maiusculas?', a.isupper())
print('Esta em minusculas?', a.islower())
print('Esta captalizada?', a.istitle())
# Print com o Metodo .format
a = input('Digite algo: ')
print('O tipo primitivo do que voce digitou é: {}\nSó tem espaços? {}'
      '\nÉ um número? {}\nÉ alfabetico? {}\nÉ alfanumerico? {}\nEsta em maiusculas? {}'
      '\nEsta em minusculas? {}\nEsta captalizada? {}'.format(type(a), a.isspace(), a.isnumeric(), a.isalpha(),
                                                              a.isalnum(), a.isupper(), a.islower(), a.istitle()))
