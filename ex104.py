# progama que analiza se o numero é inteiro ou não por meio de uma função
def leiaint(num):

    """
    :param num: recebe um valor e analiza se ele é um valor númerico e se é do tipo int
    :return: nada
    """

    if num.isnumeric() == True:
        if num != float(num):
            print(f'\033[36m O numero {num} é \033[1:32mINTEIRO\033[m')
        else:
            print(f'\033[35mErro! Digite um numero \033[1:31mINTEIRO\033[m \033[31mválido!')
            global a
            a = input('\033[33mDigite um valor')
            leiaint(a)
    else:
        print(f'\033[31mErro! Digite um numero \033[1:31mINTEIRO\033[m \033[31mválido!')
        a = input('\033[33mDigite um valor')
        leiaint(a)


a = input('\033[33mDigite um valor')
leiaint(a)
