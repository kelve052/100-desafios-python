# progama que aplica um tratamento de erro no 'ex104' consierando o valuer float tambem como numero
def leiaint(num=0, real=0):

    """
    :param num: recebe um valor e analiza se ele é um valor númerico e se é do tipo int
    :return: nada
    """

    while True:
        a = 0
        try:
            a = int(input('\033[33mDigite um valor'))
        except :
            print('\033[31mValor inteiro invalido! tente novamente: \033[m')
        else:
            num = a
            break
    while True:
        a = 0
        try:
            a = float((input('digite um numero real: ')))
        except ValueError:
            print('\033[31mValor real invalido! tente novamente: \033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuario preferio não informar um numero o valor real \033[m')
            real = 0
            break
        else:
            real = a
            break
    return num, real




a = 0
b = 0
c = leiaint(a, b)
print(f'\033[30mO numero inteiro = \033[36m{c[0]}\033[30m\n'
      f'O numero real = \033[36m{c[1]}')

