# prgama que pede 3 valores de onde iniciara e terminara a contagem e pulando de quantos em
# qauntos por meio de uma função
def pulo(a, b, d):
    c = a
    if d < 0:
        d = (d*-2/2)
    if d == 0:
        d = 1
    while c <= b:
        print('\033[34m', c, end=', ')
        c += d
    if a > b:
        c = a
        while c >= b:
            print('\033[34m', c, end=', ')
            c -= d
    print('FIM!!!')


pulo(1, 10, 1)
print()
pulo(10, 0, 2)
print()
x = int(input('\33[33mInicio: '))
y = int(input('Fim: '))
p = int(input('Pulo: '))
pulo(x, y, p)

