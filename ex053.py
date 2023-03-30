# progama que coloca a palavra de tras pra frente
a = input('digite uma frase ou palavra: ').strip().upper()
cont = len(a)
se = a.split()
junto = ''.join(se)
inverso = ''
for b in range(len(a) - 1, -1, -1):
    inverso += junto[b]
print('\033[33m', junto, '\033[30m///////\033[33m', inverso)
if inverso == junto:
    print('\033[36mÉ palindromo!')
else:
    print('\033[31mNão é palindromo!')