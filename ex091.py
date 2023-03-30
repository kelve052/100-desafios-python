# progama onde 4 jogadores jogam o dado e armazena os dandos em um dicionario e mostra o em ordem
# https://youtu.be/cwrqIztaAwk nessa aula mostra o exercicio sendo resolvido muito facil
jogadores = {}
jogadores1 = {}
maior = menor = 0
jogador = ''
cont = 1
for c in range(1, 5):
    from random import randint
    jogadores[f'jogador{c}'] = randint(1, 6)
for c, d in jogadores.items():
    print(f'{c}', end='')
    from time import sleep
    for c in range(1, 4):
        sleep(0.4)
        print('\033[35m🎲...\033[m', end='')
    sleep(0.4)
    print(f' = {d}')
sleep(1)
print('-=' * 14)
print('\033[35m===Ranking dos jogadores===\033[m')
for r in range(1, len(jogadores) + 1):
    for c, d in jogadores.items():
        if c == 'jogador1':
            maior = d
            jogador = c
        else:
            if d > maior:
                maior = d
                jogador = c
    jogadores1[jogador] = maior
    jogadores[jogador] = 0
for c,d in jogadores1.items():
    sleep(1)
    print(f'\033[30m{cont}° lugar: ', end='')
    sleep(0.25)
    print(f'{c} = {d}')
    cont += 1