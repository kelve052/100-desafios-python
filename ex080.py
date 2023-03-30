# progama que le 5 valores e os coloca em ordem sem o sort
lista = []
t = 0
cont1 = 0
a = 0
bmenor = 0
cont2 = 0
for cont in range(1, 6):
        lista.append(int(input('informe um valor: ')))
        cont2 = 0
        if t == 1:
            for c in range(1, len(lista) + 1):
                if lista[cont1] < lista[c - 1]:
                    bmenor = lista.index(lista[c - 1])
                    a = lista[cont1]
                    #print(lista, 'AM, lista[cont1] = ', lista[cont1], 'lista[c - 1] = ', lista[c - 1])
                    lista.pop(cont1)
                    lista.insert(bmenor, a)
                    print('\033[30mAdicionado na posição {} da lista\033[m'.format(bmenor + 1))
                    cont2 = 1
                    #print(lista, 'AM, lista[cont1] = ', lista[cont1], 'lista[c - 1] = ', lista[c - 1])
            if cont2 == 0:
                print('\033[30mAdicionado no final da lista...\033[m')
        cont1 = cont1 + 1
        t = 1
print('\033[33mOs valores digitados em forma ordenada cressente = ', lista)
