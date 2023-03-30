# progama que testa a velocidade permitida e se ultrapassada calcula a multa por cada km
v = float(input('informe a velocidade do carro: '))
b = v - 80
a = 7*b
if v <= 80:
    print('\033[32mvelocidade permitida!')
else:
    print('\033[33mvelocidae maxima ultrapassada!\033[m\n\033[31ma multa é de  R$7 por cada KM ultrapassado!\no valor total a pagar é R${:.2f}'.format(a))