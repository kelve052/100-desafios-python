# progama que calcula cada forma de pgamento que o susuario escolhe
valor = float(input('informe o valor do produto: '))
res = int(input('\033[32m1 - avista, cheque ou dinheiro, 10% de desconto\n\033[33m2 - avista, no cartão, 5% desconto\n\033[35m3 - em até 2x no cartão, presso normal\n\033[34m4 - 3x ou mais no cartão, 20% de juros\033[m\nqual forma de pagamento: '))
if res == 1:
    valor = valor - (valor * 10 / 100)
    print('o valor avista saira \033[32mR${}\033[m com desconto de \033[35m10%'.format(valor))
elif res == 2:
    valor = valor - (valor * 5 / 100)
    print('o valor avista no cartão saira \033[32mR${}\033[m com desconto de \033[35m5%'.format(valor))
elif res == 3:
    print('em até 2x no cartão o valor saira \033[32mR${}'.format(valor))
elif res == 4:
    valor = valor + (valor * 20 / 100)
    print('em 3x ou mais no cartão o valor saira \033[32mR${}\033[m com \033[35m20%\033[m de juros'.format(valor))
else:
    print('\033[31mopição invalida\ndigite umas das opições \033[34m(1, 2, 3 ou 4)')