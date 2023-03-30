a = int(input('qauatos dias voce alugou o carro: '))
b = float(input('quantos quilometros rodados rodados: '))
c = a*60+0.15*b
print('\033[30mo valor do aluguel do carro foi: R${}'.format(c))
