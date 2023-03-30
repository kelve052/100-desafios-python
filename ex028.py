# esse progama fala se voce adivinhou um numero entre 1 e 5 que o computador escolhe
import random

a = int(input('adivinhe um numero de 1 a 5: '))
ran = random.randint(1, 5)
if a == ran:
    print('voce gigitou \033[35m{}\033[m, \033[32mPARABEMS\033[m voce adivinhou o numero éra \033[32m{}'.format(a, ran))
elif a < 6 and a != ran and a > 0:
    print('voce gigitou \033[35m{}\033[m voce \033[31mERROU\033[m o numero éra \033[31m{}'.format(a, ran))
else:
    print('\033[31mvoce gigitou um numero diferente de 1 e 5')
