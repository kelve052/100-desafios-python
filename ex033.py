n = int(input('digitete o primeiro numero: '))
n1 = int(input('digite o segundo numero: '))
n2 = int(input('digite o terceiro numero: '))
# maneira que eu fiz
'''if n<n1:
    if n<n2:
        print('o numero {} é o menor'.format(n))
        if n1<n2:
            print('o maior numero é {}'.format(n2))
        else:
            print('o maior numero é {}'.format(n1))
    elif n1>n2:
        print('o numero maior é {}'.format(n1))
        print('o menor numero é {}'.format(n2))
    else:
        print('o numero {} é o maior'.format(n2))
        print('e o menor é {}'.format(n))
elif n>n2:
    print('o maior numeor é {}'.format(n))
    if n2>n1:
        print('o menor numero é {}'.format(n1))
    else:
        print('o menor numero é {}'.format(n2))
elif n2>n1:
    print('o maior numero é {}'.format(n2))
    print('e o menor numero é {}'.format(n1))'''
# maneira mais facil
menor = n
if n1 < n and n1 < n2:
    menor = n1
if n2 < n and n2 < n1:
    menor = n2
maior = n
if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2
print('o \033[34mmaior\033[m numero é \033[34m{}\033[m e o \033[36mmenor\033[m numero é \033[36m{}'.format(maior, menor))