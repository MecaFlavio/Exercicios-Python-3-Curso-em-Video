# Tratamento de Exceções

try:
    a = int(input('Numero 1: '))
    b = int(input('Numero 2: '))
    r = a / b
except:
    print('Infelizmente tivemos um prolblema')
else:  # parametro opcionais no tratamento de erro
    print(f'A divisão é {r}')
finally:  # também opcional no tratamento de erro
    print('Volte sempre')

# é possivel tratar o erro

try:
    a = int(input('Numero 1: '))
    b = int(input('Numero 2: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente tivemos um prolblema {erro.__class__}')  # retorna a classe do erro traceback
else:  # parametro opcionais no tratamento de erro
    print(f'A divisão é {r}')
finally:  # também opcional no tratamento de erro
    print('Volte sempre')

#  é possivel ter varios except

try:
    a = int(input('Numero 1: '))
    b = int(input('Numero 2: '))
    r = a / b
except (ValueError, TypeError):
    print('Problemas com tipos de dados digitados')  # mensagem de erro personalizado
except ZeroDivisionError:
    print('Não é possivel divisão por zero')
except KeyboardInterrupt:
    print('O usuario não informou dados')
else:  # parametro opcionais no tratamento de erro
    print(f'A divisão é {r}')
finally:  # também opcional no tratamento de erro
    print('Volte sempre')