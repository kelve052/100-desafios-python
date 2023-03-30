# progama que analiza comprar e da informações no final
total = 0
pmm = 0
barato = 0
precomenor = 99999999
while True:
    nome = str(input('\033[30mQual o nome do produto: '))
    preco = float(input('Qual o preço do produto: \033[m'))
    if preco > 1000:
        pmm = pmm + 1
    if preco < precomenor:
        barato = nome
        precomenor = preco
    total = total + preco
    op = str(input('Quer continuar a comprar? [S] [N]')).upper()
    if op == 'N':
        break
print('''\033[34m====================================================\033[m\nO presso total dos produtos é \033[32mR${}!\n\033[34m{}\033[m produtos custam mais de \033[32mR$1000!
\033[mO nome do produto mais barato é \033[32m{}!\n\033[34m====================================================\033[m'''.format(total, pmm, barato))
