# Crie um código em python que teste se o site pudim.com.br está acessivel pelo computador usado
import urllib
import urllib.request
try:
    pagina = urllib.request.urlopen('http://www.pudim.com.br')
except Exception as erro:
    print(f'O site Pudim não esta acessivel no momento {erro.__class__}')  # assim testo o erro que o try retorna
else:
    print('O site pudim está acessivel atualmente')
