# progama que le varios valores e por meuiu de uma função ele fala quantos valores foram lidos
# e qual é o maior
from time import sleep


def maior(*valores):
    sleep(1)
    for c in range(1, len(valores) + 1):
        sleep(0.3)
        print(valores[c-1], end=' ')
    print()
    print(f'\033[30mForam passados \033[33m{len(valores)}\033[30m valores\n e o maior valor foi o \033[33m{max(valores)}')
    print('\033[31m=\033[m' * 26)


print('Analizando valores', end='')
for c in range(1, 4):
    sleep(0.8)
    print('.', end='')
print()
print('\033[31m=\033[m' * 26)
maior(1, 2, 7)
maior(5, 55, 55)
maior(7, 45, 458, -5, 0)
maior(-5, -7, -154, -9, -2)
maior(4, 0)
