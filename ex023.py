# progama que mostra a casa de cada numero seja unidade desenna centena...
numero = int(input('digite um numero de 0 à 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('\033[32;40munidade {}'.format(u))
print('\033[33;40mdezena {}'.format(d))
print('\033[34;40mcentena {}'.format(c))
print('\033[35;40mminlhar {}'.format(m))
