# progama que le varios valores ate digitar 999 para parar e soma todos menos o 999
a = int(input('digite um valor: '))
b = 0
cont = 0
while a != 999:
    b = b + a
    a = int(input('digite um valor: '))
    cont += 1
print('\033[34ma soma dos valores digitados enquanto o progama estava rodando é {}\n\033[32mO total de valores digitados foi {}'.format(b, cont))