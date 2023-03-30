a = float(input('digite o salario do funcionario: '))
b = a+(a*15/100)
print('o  salario do funcionario é de \033[32mR${}\033[m e com \033[35m15%\033[m de almento seu salario será \033[36m{}R$'.format(a, b))
