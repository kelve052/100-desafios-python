largura = float(input('informe a largura em metros da parede: '))
altura = float(input('informe a altura em metros da parede: '))
area = largura*altura
tinta = area/2
print('os valores informados foi: \n\033[32mlargura = {}\033[m\n\033[32maltura = {}\033[32m\n\033[35me sera nessesario \033[1;36m{}\033[m \033[35mlitros de tinta para pintar a parede.'.format(largura, altura, tinta))
