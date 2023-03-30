# progama que analiza o menor e o maior peso inserido
print('\033[33minforme o peso de 5 pessoas')
peso1 = 0
peso2 = 5000
for cont in range(1, 6):
    peso = float(input('\033[34mpeso: '))
    if peso > peso1:
        peso1 = peso
    elif peso < peso2:
        peso2 = peso
print('\033[37mPeso menor peso: {}!\nPeso maior peso: {}!'.format(peso2, peso1))