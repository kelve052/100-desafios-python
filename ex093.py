# progama que faz o gerenciamento do jogador de futebol
jogador = dict()
listgol = list()
total = 0
jogador['nome'] = str(input('\033[31mnome do jogador: '))
jogador['partidas'] = int(input(f'Quastas partidas {jogador["nome"]} jogou: '))
for c in range (1, jogador['partidas'] + 1):
    listgol.append(int(input(f'Quantos gols ele fez na partida {c}: ')))
jogador['gols'] = listgol
jogador['total'] = 0
for d in range(1, len(listgol) + 1):
    jogador['total'] = jogador['total'] + listgol[d - 1]
print('\033[33m__\033[m' * 35)
print(f'\033[37m{jogador}\033[m')
for c, d in jogador.items():
    print(f'O campo \033[1:31m{c}\033[m tem o valor \033[1:31m{d}\033[m')
print('\033[33m__\033[m' * 35)
print(f'O jogador \033[1:31m{jogador["nome"]}\033[m jogou \033[1:31m{jogador["partidas"]} partidas\033[m')
for c in range(1, len(jogador['gols']) + 1):
    print(f'Na partida \033[1:31m{c}\033[m ele fez \033[1:31m{jogador["gols"][c - 1]}\033[m gosl!')
print('\033[33m__\033[m' * 35)