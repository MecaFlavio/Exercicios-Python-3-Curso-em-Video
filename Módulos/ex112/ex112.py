# Dentro do pacote utilidadeCeV que criamos do desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar com a função
# input(), mas com uma validação de dados para aceitar apenas valores que sejam monetarios
from utilidadescev import moeda
from utilidadescev import dados

valor = dados.leiaDinheiro('Digite um valor: R$ ')
moeda.resumo(valor, 5, 5)
