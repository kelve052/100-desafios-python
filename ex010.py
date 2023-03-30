a = float(input('informae quantos reais tem na carteira: '))
b = a % 3.27
c = a // 3.27
print('voce tem \033[33mR${}\033[m e da pra comprar \033[35mU${}\033[m e sobra \033[33mR${}'.format(a, c, b))
