lista = []
nome = []
notas = []
while True:
    nome.append(str(input('\033[33mNome: \033[m')))
    notas.append(float(input('\033[36mNota1: \033[m')))
    notas.append(float(input('\033[36mNota2: \033[m')))
    nome.append(notas[:])
    lista.append(nome[:])
    nome.clear()
    notas.clear()
    op = str(input('Quer continuar a cadastrar? [S/N]')).upper()
    if op == 'N':
        break
a = 'N° Alunos'
print('-'*35)
print(f'\033[1:30m{a:<23}Média\033[m')
print('-'*35)
for c in range(1, len(lista) + 1):
    print(f'\033[30m{c - 1}  \033[33m{lista[c - 1][0]:<23}\033[36m{(lista[c - 1][1][0] + lista[c - 1][1][1]) / 2:.1f}\033[m')
while True:
    op = int(input('Desesa mostrar as notas de qual aluno?[999 para interromper]'))
    if op == 999:
        break
    else:
        for c in range(1, len(lista) + 1):
            if op == c - 1:
                print(f'Notas de \033[33m{lista[c - 1][0]}\033[m: \033[36m{lista[c - 1][1]}\033[m!')