# progama que faz o fatorial com um apigrud por meio de função
def fatorial(a, shol=False):
    """
    :param a: o numero a ser analizado para o fatorial
    :param shol: pra true se deseja mostrar o calculo e false pra não mostrar
    :return: retorna fatorial
    """
    g = a
    s = a
    if shol == False:
        for c in range(1, a):
            a = a - 1
            s = s * a
        return s
    else:
        print(g, end=' ')
        for c in range(1, a):
            a = a - 1
            print(f'x {a}', end=' ')
            s = s * a
        return f' = {s}'


x = fatorial(5, True)
print(x)