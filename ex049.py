# tabuada usando laço
n = int(input('insira um valor: '))
for a in range(0, 10):
    a = a+1
    b = n * a
    print('{} x {} = {}'.format(n, a, b))