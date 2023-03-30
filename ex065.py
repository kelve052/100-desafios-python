# progama que le valores enquanto diser sim e depois mosra o maior e menor e a media deeles
res = 'S'
cont = 0
a = 0
maior = 0
menor  = 9999999
b = 0
while res == 'S':
    a = int(input('\033[30minforme um valor: \033[m'))
    res = str(input('\033[32mDeseja continuar? \033[33m[N], [S]\033[m')).upper()
    if a > maior:
        maior = a
    if a < menor:
        menor = a
    cont += 1
    b = b + a
media = b / cont
print('a media de todos os valores digitados foi {}'.format(media))
print('\033[34mO maior numero foi {}!\n\033[33mO menor numero foi {}!'.format(maior, menor))