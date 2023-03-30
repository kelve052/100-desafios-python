# progama que tira o fatorial de um valor
a = int(input('informe um valor: '))
b = a
t = a
# USANDO WHILE
while b != 1:
    b -= 1
    a = a * b
print('fatorial de \033[33m{}\033[m é \033[32m{}\033[m!'.format(t, a))
# USANDO FOR (PRA O FOR FUNCIONAR O WHILE DEVE SER COMENTADO)
for b in range(b, 1):
    a -= 1
    print(t, b, a)
    t = t * a
print('fatorial de \033[33m{}\033[m é \033[32m{}\033[m!'.format(b, t))
