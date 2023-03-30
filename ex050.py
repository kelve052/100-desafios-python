# progama que le 6 valores e soma apenas os numeros que forem pares
b = 0
for a in range(1, 7):
    a = int(input('gitite um valor: '))
    if a % 2 == 0:
        b = b + a
print('a soma dos numeros pares é \033[36m{}'.format(b))

