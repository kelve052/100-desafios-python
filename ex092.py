# progama que le muitos valores sobre a pessoa e mostra outros dados
pessoa = {}
from datetime import date
data = date.today().year
pessoa['nome'] = str(input('\033[34mNome: '))
pessoa['data_nacimento'] = (int(input('Data de nacimento: ')))
pessoa['idade'] = data - pessoa['data_nacimento']
pessoa['carteira'] = int(input('Carteira de trabalho \033[1m[0 não tem]\033[m:'))
if pessoa['carteira'] == 0:
    print('\033[30m-=\033[m' * 40)
    print(f'\033[37mInformações da pessoa: {pessoa}\033[m')
    for c, d in pessoa.items():
        x = ''
        if c == 'carteira':
            x = 'N°: '
        print(f'\033[33m{c} é {x}{d}!\033[m')
else:
    pessoa['ano_de_contrato'] = int(input('\033[34mAno de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['ano_aposentado'] = (pessoa['ano_de_contrato'] + 35) - pessoa['data_nacimento']
    print('\033[30m-=\033[m' * 40)
    print(f'\033[37mInformações da pessoa: {pessoa}\033[m')
    for c, d in pessoa.items():
        if c == 'carteira':
            x = 'N°: '
        else:
            x = ''
        print(f'\033[33m{c} é {x}{d}')
print('\033[30m-=' * 40)