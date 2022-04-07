# Faça um programa que tenha uma funçao notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informaçoes:
# - Quantidade de notas
# - A maior nota
# - a menor notas
# - a média da turma
# - a situação (opcional)
# Adicione também as docstrings da função.
def notas(*d, sit=False):
    """
    Analisa notas e situação de varios alunos
    :param d: recebe varios valores
    :param sit: parametro opcional, original False
    :return: quantidade de notas, maior nota, menor nota, media de notas e situação da turma
    """
    r = dict()
    r['total'] = len(d)
    r['maior'] = max(d)
    r['menor'] = min(d)
    r['média'] = sum(d) / len(d)
    if sit:
        if r['média'] >= 7:
            r['situção'] = 'BOA'
        elif r['média'] >= 5:
            r['situção'] = 'RAZOAVEL'
        else:
            r['situção'] = 'RUIM'
    return r


#programa principal
resp = notas(10, 2.5, 4, 7.8, 2, 3.5, sit=True)
print(resp)
help(notas)
