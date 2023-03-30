# progama que le a idade de uma pessoa e avalia o voto dela por meio de uma função com str mesclada no global


def ano(idade):
    from datetime import date
    idade = date.today().year - idade
    if idade < 17:
        f = '\033[1:32mNEGADO!'
    elif idade == 17 or idade > 63:
        f = '\033[1:33mOPICIONAL!'
    else:
        f = '\033[1:31mOBRIGATÓRIO!'
    return f


idade1 = int(input('Informe a data de nascimento do cidadão: '))
k = ano(idade1)
print(f'\033[30mDireito de voto ao cidadão: {k}')