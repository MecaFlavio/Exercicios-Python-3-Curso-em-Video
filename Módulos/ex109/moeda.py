def aumentar(p, t, f=False):
    """
    Aumenta um valor numa porcentagem.
    :param p: Preço float
    :param t: Taxa
    :param f: False (parametro opcional). True para receber formatação da função moeda()
    :return: Valor com aumento da taxa
    """
    res = p + (p * t/100)
    return res if not f else moeda(res)


def diminuir(p, t, f=False):
    """
    Reduz um valor em uma porcentagem
    :param p: preço float
    :param t: taxa
    :param f: False (parametro opcional). True para receber formatação da função moeda()
    :return: valor com desconto da taxa
    """
    res = p - (p * t/100)
    return res if f is False else moeda(res)  # essa linha tem o mesmo sentido da linha 3


def dobro(p, f=False):
    """
    Dobra um valor.
    :param p: Preço float
    :param f: False (parametro opcional). True para receber formatação da função moeda()
    :return: Valor dobrado
    """
    res = p * 2
    return res if not f else moeda(res)


def metade(p, f=False):
    """
    Reduz um valor pela metade
    :param p: Preço float
    :param f: False (parametro opcional). True para receber formatação da função moeda()
    :return: Metade do valor
    """
    res = p / 2
    return res if not f else moeda(res)


def moeda(p, moeda='R$ '):
    """
    Formata valor
    :param p: Preço float
    :param moeda: sigla da moeda string
    :return: valor formatado numa fstring
    """
    return f'{moeda}{p:.2f}'.replace('.', ',')
