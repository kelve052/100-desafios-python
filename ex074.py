# progama que gera 5 numeros aleatorios e guarda uma tupla e mostra o menor e maior
from random import randint
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
maior = 0
menor = 11
for c in range(1,6):
    a = randint(1,10)
    if a > maior:
        maior = a
    if a < menor:
        menor = a
    if c == 1:
        n1 = a
    if c == 2:
        n2 = a
    if c == 3:
        n3 = a
    if c == 4:
        n4 = a
    if c == 5:
        n5 = a
        tupla = (n1, n2, n3, n4, n5)
        print('\033[30m=' * 34)
        print(f'\033[34:40mOs numeros foram {tupla}!\033[m\n\033[34:40mO numero maior é {maior}\033[m')
        print('\033[34:40mO numero menor é {menor}!\033[m')
print('\033[30m='*34)
#print(f'\033[34:40mO numero menor é {min(menor)}!\033[m')
#print(f'\033[34:40mO numero menor é {max(maior)}!\033[m') tambem da pra ver o maior e menor dessas formas