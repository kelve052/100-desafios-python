lista = []
posimaior = 0
posimenor = 0
maior = 0
menor = 999
for cont in range(1, 6):
    lista.append(int(input(f'\033[30mdigite um valor {cont}: ')))
    if lista[cont-1] > maior:
        posimaior = cont
        maior = lista[cont - 1]
    if lista[cont - 1] < menor:
        posimenor = cont
        menor = lista[cont - 1]
print('\033[36m='*35)
print(f'\033[33mOs valores digitados foram: {lista}')
print('\033[36m='*35)
print(f'\033[30mO maior valor foi {max(lista)} na posição {posimaior}')
print(f'O menor valor foi {min(lista)} na posição {posimenor}')
print('\033[36m='*35)