# prgam que tem duas função uma é sortear 5 valores e por na lista e a outra é somar os valores pares
def sortear(list1):
    from random import randint
    for c in range(1, 6):
        x = randint(1, 10)
        list1.append(x)
    print(f'A lista sorteada foi: \033[33m{list1}\033[m')


def par(list1):
    a = 0
    for c in range(1, len(list1) + 1):
        if list1[c - 1] % 2 == 0:
            a += list1[c - 1]
    print(f'a soma dos valores pares da lista é: \033[33m{a}\033[m')



lista = []
sortear(lista)
par(lista)
