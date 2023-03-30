# progama que le nome sexo e idade de pessoas e colaca dada uma em um dicionario e todos os dicionarios em uma lista
pessoa = {}
lista = []
mediaidade = 0
mediaidade1 = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    op = str(input('Quer continuar a cadastrar? \033[31M(S/N)\033[M ')).upper()
    if op == 'N':
        break
print('\033[34m// \033[m' * 21)
print(f'\033[33mForam cadastradas {len(lista)} pessoas!')
for c in range(1, len(lista) + 1):
    for c, d in lista[c - 1].items():
        if c == 'idade':
            mediaidade1 += 1
            mediaidade = mediaidade + d
print(f'\033[33mA média da idade das pessoas cadastradas é {mediaidade / mediaidade1}!')
print('\033[34m-\033[m' * 60)
print('\033[33mAs pessoas com sexo feminino foram: ', end='')
for c1 in range(1, len(lista) + 1):
    for c, d in lista[c1 - 1].items():
        if d == 'F':
            print(lista[c1 - 1]['nome'], end=' ')
print()
print('\033[34m-\033[m' * 60)
print('\033[33mAs pessoas com idade assima da média do grupo são: ')
for c2 in range(1, len(lista) + 1):
    for c, d in lista[c2 - 1].items():
        if c == 'idade':
            if d >= (mediaidade / mediaidade1):
                print(f'Nome: {lista[c2 - 1]["nome"]}, {c}: {d}, sexo: {lista[c2 - 1]["sexo"]}')
print('')
print('\033[34m// ' * 21)