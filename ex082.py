# progama que le valores e depois divide os pares e impares em mais duas listas 1-codco 1 2-codco 2
# codico2 ele le tudo e depois divide/ codico1 ele e ja separa emquanto esta lendo
a = input('1 ou 2')
if a == '1':
    lista = []
    par = []
    impar = []
    cont = 0
    a = '\033[32m'
    b = '\033[33m'
    while True:
        lista.append(int(input('\033[30mDigite um valor:\n[999 para parar]\033[m')))
        if 999 in lista:
            break
        if lista[cont] % 2 == 0:
            par.append(lista[cont])
        else:
            impar.append(lista[cont])
        cont += 1
    print(f'Os valores digitados foram {lista}')
    print(f'\033[36mOs valores pares são {par}!\n\033[34mOs valores impares são {impar}!')
if a == '2':
    lista = []
    par = []
    impar = []
    cont = 0
    a = '\033[32m'
    b = '\033[33m'
    while True:
        lista.append(int(input('\033[30mDigite um valor:\n[999 para parar]\033[m')))
        if 999 in lista:
            break
    for c in range(1, len(lista) + 1):
        if lista[c - 1] % 2 == 0:
            par.append(lista[c - 1])
        else:
            impar.append(lista[c - 1])
    print(f'Os valores digitados foram {lista}')
    print(f'\033[36mOs valores pares são {par}!\n\033[34mOs valores impares são {impar}!')