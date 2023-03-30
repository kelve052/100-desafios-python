# progama que cria uma função de calcular area do terreno
def area(a, b):
    s = a * b
    print(f'\033[36mA area do terreno \033[35m{a}\033[36mx\033[35m{b}\033[36m é \033[35m{s}m2!')


a = float(input('\033[30mInforme a largura do terreno: '))
b = float(input('Informe o comprimento do terreno: '))
area(a, b)