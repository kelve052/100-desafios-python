# prgama que analiza o nome e quantidades de gols de um jogador pror meio de função
def ficha(nome, gol=0):
    if nome == '':
        nome = 'Desconhecido'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    return nome, gol


x = ficha(str(input('Nome do jogador: ')), str(input(f'quantidade de gols: ')))
print(f'{x[0]} fez {x[1]} gols no campeonato!')