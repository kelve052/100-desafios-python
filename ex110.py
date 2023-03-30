# progama que faz um modulo continuação do ex109 melhorado

def resumo(p, almento, diminuimento):
    almento = almentar(p, almento)
    diminuimento = diminuir(p, diminuimento)
    dobro1 = dobro(p)
    metade1 = metade(p)
    return print(f'{"Valor analizado: ":<35}\033[32m{p:.2f}R$\033[m\n{"Valor depois do almento ":<35}\033[32m{almento:.2f}R$\033[m\n{"Valor depois da diminuição ":<35}'
                 f'\033[32m{diminuimento:.2f}R$\033[m'
                 f'\n{"Valor dobrado ":<35}\033[32m{dobro1:.2f}R$\033[m\n{"Metade do Valor ":<35}\033[32m{metade1:.2f}R$\033[m')






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
