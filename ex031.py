# progama que ve o valor a pagar dependendo da distancea que sera a viagem
d = float(input('qual é a distancea da viagem em KM: '))
a = d*0.50
b = d * 0.45
if d <= 200:
    print('o valor da viagem custará \033[32mR${}'.format(a))
else:
    print('a distancea e maior que \033[33m200KM\033[m então o valor da viagem custára \033[32mR${}'.format(b))