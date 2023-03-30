# progama vendo quanstas letras "a" tem e em que local a primeira e ultima ela aparece
frase = input('digite uma frase: ').strip()
frase2 = frase.upper().strip()
print('a frase digitada tem \033[33m{}\033[m letras "\033[33ma\033[m"'.format(frase2.count('A')))
print('o primeiro "\033[33ma\033[m" ta na posição \033[33m{}\033[m'.format(frase2.find('A')+1))
print('e o ultimo "\033[33ma\033[m" ta na posição \033[33m{}'.format(frase2.rfind('A')+1))
