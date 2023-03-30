n = int(input('digite um numero: '))
e = int(input('escolha a base de converção:\n1-binario\n2-octal\n3-hexadecimal\n'))
if e == 1:
    print('o numero \033[34m{}\033[m convertido em \033[35mbinario\033[m é \033[35m{}'.format(n, bin(n)))
elif e == 2:
    print('o numero \033[34m{}\033[m convertido em \033[35mactal\033[m é \033[35m{}'.format(n,oct(n)))
elif e == 3:
    print('o numero \033[34m{}\033[m convertido em \033[35mhexadecimal\033[m é \033[35m{}'.format(n, hex(n)))
else:
    print('\033[31mopição invalida!')