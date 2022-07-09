# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# num arquivo de teste simples
# O sistema só vai ter 2 opçoes: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas

# o asterisco no import indica que toda lib foi importada

from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    respostas = menu(['Ver Cadastro', 'Cadastrar Pessoas', 'Excluir Arquivo', 'Sair'])
    if respostas == 1:
        cabeçalho('Visualização de Cadastro')
        lerArquivo(arq)
    elif respostas == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif respostas == 3:
        delArquivo(arq)
    elif respostas == 4:
        cabeçalho('SAINDO DO SISTEMA! ATÉ LOGO...')
        break
    else:
        cabeçalho('\033[1;101mErro! Digite uma opção valida.\033[0m')
    sleep(2)
