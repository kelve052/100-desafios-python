# aprimoramento do (ex.093)
lista = list()
jogador = dict()
listgoll = list()
r = 0
while True:
    r += 1
    jogador['cod'] = r
    jogador['nome'] = str(input('\033[34mNome: '))
    cont = jogador['partidas'] = int(input(f'quantas partidas \033[36m{jogador["nome"]}\033[34m jogou: '))
    for c in range(1, cont + 1):
        listgoll.append(int(input(f'quantos goll ele fez na \033[36m{c}°\033[34m partida: ')))
    jogador['goll'] = listgoll.copy()
    jogador['total'] = 0
    for c in range(1, cont + 1):
        jogador['total'] = jogador['total'] + listgoll[c - 1]
    lista.append(jogador.copy())
    listgoll.clear()
    op = str(input('quer adicionar mais um jogador? (S/N)')).upper()
    if op == 'N':
        break
print('\033[30m-\033[m' * 52)
a = 'cod - jogador'
b = 'partidas'
c = 'gols'
d = 'total'
espaco = 20
print(f'{a:<25}{c:<20}{d}')
print('\033[37m', lista, '\033[m')
print('\033[30m-\033[m' * 52, end='')
for c in range(1, len(lista) + 1):
    print()
    for c1, d1 in lista[c - 1].items():
        if c1 == 'cod':
            print(end='')
            espaco = 5
        else:
            espaco = 20
        if c1 != 'partidas':
            print(f'{f"{d1}":<{espaco}}', end='')
print()
print('\033[30m-\033[m' * 52)
while True:
    op = int(input('\033[33mMostrar dados de qual jogador? (999 para finalizar) '))
    if op == 999:
        print('\033[30m-\033[m' * 52)
        break
    elif op <= len(lista) and op > 0:
        print(f'levantamento do jogador {lista[op - 1]["nome"]}')
        for c in range(1, len(lista[op - 1]['goll']) + 1):
            print(f'na partida {c} ele fez {lista[op - 1]["goll"][c - 1]} gols')
    else:
        print('\033[31mO codco de jogador não existe tente novamente!\033[m')
    print('\033[30m-\033[m' * 52)
print('\033[1mFinalizado!!!')