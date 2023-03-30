# progama que fala se o valor e primo ou não
a = int(input('\033[30mdigite um valor: '))
cont = 0
for b in range(1, a+1):
    if a % b == 0:
        print('\033[36m{}'.format(b), end=' ')
        cont = cont + 1
    else:
        print('\033[31m{}'.format(b), end=' ')
if cont < 3:
    print('\n\033[34mO numero {} foi dividido {} veses \n\033[34mé primo'.format(a, cont))
else:
    print('\n\033[34mO numero {} foi dividido {} veses \n\033[31mnão é primo'.format(a, cont))
