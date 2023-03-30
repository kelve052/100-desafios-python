r1 = float(input('informe a primeira reta: '))
r2 = float(input('informe a segunda reta reta: '))
r3 = float(input('informe a terceira reta: '))

if (r1+r2)>r3>(r1-r2) and (r2+r3)>r1>(r2-r3) and (r1+r3)>r2>(r1-r3):
    print('\033[32mÉ possivel formar um triangulo!')
    if r1 == r2 == r3:
        print('\033[36mEquilátero!')
    elif r1 != r2 != r3:
        print('\033[36mEscaleno!')
    else:
        print('\033[36mIsóseles!')
else:
    print('\033[31mNão é possivel formar um triangulo!')
