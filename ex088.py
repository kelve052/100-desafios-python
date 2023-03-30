# progama que pergunta quantos jogos quer gerar e cada jogo vem com 6 numero aleatorios cada jogo e uma
# lista e todos dentro de uma unica lista
lista = []
jogo = []
op = int(input('quantos jogos voce quer palpitar? '))
for c in range(1, op + 1):
    c1 = 1
    import random
    while c1 < 7:
        a = random.randint(1, 60)
        if a not in jogo:
            jogo.append(a)
            c1 += 1
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
for c in range(1, len(lista) + 1):
    import time
    time.sleep(1)
    print(f'\033[30mjogo {c}->\033[m {lista[c - 1]}')