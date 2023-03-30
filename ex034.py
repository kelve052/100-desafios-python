# progama que fala o almento em % do salario de acordo com a quantidade de salario que o funcionario tem
s = float(input('informe o salrio: '))
if s <= 1250:
    almento = s+(s*15/100)
    print('o salario de \033[33mR${}\033[m, com \033[32malmento\033[m de \033[35m15%\033[m será \033[32mR${}'.format(s, almento))
else:
    almento = s+(s*10/100)
    print('o salario de R$  \033[33m{}\033[m, com \033[32malmento\033[m de \033[35m10%\033[m será \033[32mR${}'.format(s, almento))