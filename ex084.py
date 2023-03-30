# analisa pessoas e seus pesos cada pessoa em uma lista dentro de outra lista.
pessoas = []
dado = []
while True:
    dado.append(str(input('\033[30mNome: ')))
    dado.append(float(input('\033[30mPeso: \033[m')))
    pessoas.append(dado[:])
    dado.clear()
    op = str(input('\033[34mQuer continuar a cadastrar?\033[1:30m[S, N]\033[m')).upper()
    if op == 'N':
        break
print('\033[1:30m_\033[m'*40)
print(f'\033[33mForam cadastradas: {len(pessoas)} pessoas!\033[m')
print('\033[33mAs pessoas mais pesadas (+90kg) são: ', end='')
for c in range(1, len(pessoas) + 1):
    if pessoas[c - 1][1] >= 90:
        print('\033[1:30m', pessoas[c - 1][0], end='\033[m')
print('\n\033[32mAs pessoas mais leves (-90kg) são: ', end='')
for c in range(1, len(pessoas) + 1):
    if pessoas[c - 1][1] < 90:
        print('\033[1:30m ', pessoas[c - 1][0], end='')
print('\n', end='')
print('\033[1:30m_\033[30m'*40)