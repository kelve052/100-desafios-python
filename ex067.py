# tabuada (melhorada usando break)
while True:
    a = int(input('\033[33mqual valor voce quer saber a tabuda: '))
    y = 1
    if a < 0:
        break
    for cont in range(1, 11):
        x = a * y
        print(f'\033[30m{a} x {y} = \033[36m{x}')
        y += 1
print('\033[35mFim da execução!')