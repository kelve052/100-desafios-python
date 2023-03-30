# aprimoramento do ex86
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
par = 0
maior = 0
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
    print(f'\033[36m{lista[c - 1]}\033[m', end='')
    if c == 3 or c == 6:
        print('\n', end='')
print('\n',end='')
print('_'*40)
for cont in range(1, len(lista) + 1):
    maior = lista[3][0]
    if lista[cont - 1][0] % 2 == 0:
        par = par + lista[cont - 1][0]
    if lista[4][0] > maior:
        maior = lista[4][0]
    if lista[5][0] > maior:
        maior = lista[5][0]
print(f'A soma dos numeros pares é: \033[32m{par}\033[m')
print(f'A soma dos valores da teceira coluna é: \033[32m{lista[2][0] + lista[5][0] + lista[8][0]}\033[m')
print(f'O maior valore da segunda linha é: \033[32m{maior}\033[m')
print('_'*40)

