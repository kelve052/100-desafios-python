# progama que le varios valores e os coloca em lista e mostra em ordem decressente
lista = []
cont = 0
cont1 = 2
t = 0
a = 0
while True:
    lista.append(int(input('\033[34mInforme um valor: ')))
    if t == 1:
        for c in range(1, cont1-1):
            if a == 0:
                if lista[cont] == lista[c - 1]:
                    lista.pop(cont)
                    a = 1
                    cont1 = cont1 - 1
                    cont = cont - 1
    a = 0
    t = 1
    cont = cont + 1
    cont1 += 1
    op = str(input('quer continuar a cadastrar valores? ')).upper()
    if op == 'N':
        break
lista.sort()
print('¨'*35)
print(f'Os valores digitados foram {lista}')
print('¨'*35)