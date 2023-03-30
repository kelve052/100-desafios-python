# progama que ver qual valor é maior ou se são iguais
a = int(input('informe o primeiro valor: '))
b = int(input('informe o segundo valor: '))
if b > a:
    print('o valor maior é \033[32m{}'.format(b))
elif b == a:
    print('\033[33mnão existe valor maior, os dois valores são iguais')
else:
    print('o valor maior é \033[32m{}'.format(a))
