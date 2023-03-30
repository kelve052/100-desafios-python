# progama que analiza uma expreção e ve se ta serta de acordo com os parentezes
lista = []
lista.append(str(input('digite uma expreção')))
lista = lista[0].strip()
cont1 = lista.count('(')
cont2 = lista.count(')')
if cont1 == cont2:
    if lista[0].strip() == ')':
        print('\033[31mexpreção errada')
    else:
        print('\033[36mexpreção correta!')
else:
    print('\033[31mexpreção errada!')
