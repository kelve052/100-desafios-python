# prgama que melhora o 61 perguntando se que mostrar mais termos
p = int(input('informe o primeiro termo da PA: '))
r = int(input('informe a razão: '))
cont = 1
while cont != 11:
    print(p)
    p = p + r
    cont += 1
    if cont == 11:
        op = int(input('\033[30mvoce quer mostrar mais quantos termos?'))
        if op != 0:
            cont = cont - op