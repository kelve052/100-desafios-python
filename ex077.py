# progama que pega as palavras de tupla e mostras as vogais delas
tupla = ('culto', 'temor', 'orgia', 'sendo', 'censo', 'mundo', 'denso', 'pauta',
         'fugaz', 'valha', 'cozer', 'neném', 'ainda', 'cadeira')
print('\033[30m-\033[m'*45)
for c in range(1, (len(tupla))+1):
    print(f'\nA palavra \033[30m{tupla[(c)-1]}\033[m temos as vogal:', end='')
    for n in tupla[c-1]:
        if n in 'aeiou':
            print('\033[32m', n, end='\033[m')
print('')
print('\033[30m-'*45, end='')