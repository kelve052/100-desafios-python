# progama que faz um modulo para mostrar de forma mais bonita o ex107
def moeda(v):
    v = f'\033[32m{v:.2f}R$\033[m'
    return v




#ex107




def almentar(v, almento):
    v += almento
    return v


def diminuir(v, diminuir):
    v -= diminuir
    return v


def dobro(v):
    v *= 2
    return v


def metade(v):
    v /= 2
    return v