# progama que é igual ao 108 entretando usando False ou True ecolocando o 107 aqui dentro
def moeda(v):
    return v


def moeda1(v):
    v = f'\033[32m{v:.2f}R$\033[m'
    return v


# ex107


def almentar(v, almento, formatacao_moeda = False):
    v += almento
    if formatacao_moeda == False:
        return v
    else:
        return moeda1(v)


def diminuir(v, diminuir, formatacao_moeda = False):
    v -= diminuir
    if formatacao_moeda == False:
        return v
    else:
        return moeda1(v)


def dobro(v, formatacao_moeda = False):
    v *= 2
    if formatacao_moeda == False:
        return v
    else:
        return moeda1(v)


def metade(v, formatacao_moeda = False):
    v /= 2
    if formatacao_moeda == False:
        return v
    else:
        return moeda1(v)
