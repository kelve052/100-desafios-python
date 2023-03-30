# progama que registra pessoas e suas idades (muitos lupps de opiçõe pra caso o usuario errar)
lup1 = 0
lup2 = 0
lup3 = 0
masc = 0
fem = 0
maior = 0
while lup1 == 0:
    idade = int(input('\033[30minforme a idade: \033[m'))
    if idade > 18:
        maior = maior + 1
    lup1 = 1
    lup2 = 0
    while lup2 == 0:
        sexo = str(input('\033[30minforme o sexo: \033[34m[F] [M]\033[m')).upper()
        if sexo == 'M':
            masc = masc + 1
            lup2 = 1
            lup3 = 0
            lup1 = 0
        elif sexo == 'F':
            if idade < 20:
                fem = fem + 1
            lup2 = 1
            lup3 = 0
            lup1 = 0
        else:
            lup2 = 0
            lup3 = 1
        while lup3 == 0:
            op = str(input('Quer continuar a registrar? \033[34m[S] [N]\033[m')).upper()
            if op == 'N':
                lup1 = 1
                break
            elif op == 'S':
                lup1 = 0
                break
print('''\033[30m===============================
\n\033[34mForam cadastrados {} homesm!\n\033[36mForam cadastradas {} mulheres com menos de 20 anos!
\n\033[33m Tem {} pessoas com menos de 20 anos!'''.format(masc, fem, maior))
