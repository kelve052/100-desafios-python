# progama que simula uma mtris de 3x3 e cada item é uma lista
lista = []
a1 = []
a2 = []
a3 = []
b1 = []
b2 = []
b3 = []
c1 = []
c2 = []
c3 = []
lista = [[a1], [a2], [a3], [b1], [b2], [b3], [c1], [c2], [c3]]
a = 0
b = 0
for c in range(1, 10):
    lista[c-1].clear()
    lista[c-1].append(int(input(f'Informe um valor para[{a} {b}]')))
    b += 1
    if c == 3:
        a = 1
        b = 0
    if c == 6:
        a = 2
        b = 0
print('_'*35)
for c in range(1, len(lista) + 1):
    print(f'\033[36m{lista[c - 1]}', end='')
    if c == 3 or c == 6:
        print('\n', end='')