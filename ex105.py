# le varias notas e dentro de uma função as coloca em um dicionário e exibe informações
def notasalunos(*notas, sit=False):
    """

    :param notas: notas dos alunos a serem analizadas
    :param sit: para mostrar a situação da turma
    :return: os dados da turma: maior nota, menor nota, media, quentidade de notas e o dicionario completo
    """
    dicionario = dict()
    maiornota = 0
    menornota = 0
    media = 0
    situacao = ''
    for c in range(1, len(notas) + 1):
        dicionario[f'nota{c}'] = notas[c - 1]
    quantidade = len(dicionario)
    for i, y in dicionario.items():
        if y == max(dicionario.values()):
            maiornota = i, y
        if y == min(dicionario.values()):
            menornota = i, y
        media += y
    media = media / len(dicionario)
    if media < 6:
        situacao = '\033[31:1mRuim!\033[m'
    elif media < 7:
        situacao = '\033[33:1mBoa!\033[m'
    else:
        situacao = '\033[32:1mÓtima!\033[m'
    if sit != True:
        return dicionario, quantidade, maiornota, menornota, media,
    else:
        return dicionario, quantidade, maiornota, menornota, media, print(f'Situação da turma: {situacao}')


x = notasalunos(6, 8, 5.9, 7, 10, 9, sit=True)
print('=/' * 44)
print(f'\033[30mDicionario: \033[33m{x[0]}!\033[31m\n\033[30mquantidade: \033[33m{x[1]}!\033[30m\n'
      f'\033[30mMaior nota: \033[33m{x[2]}'
      f'!\033[30m\n\033[30mMenor nota:\033[33m {x[3]}!\033[30m\n\033[30mMédia da turma: \033[33m{x[4]}\033[m')

x = notasalunos(7, 8, 7.9, 7, 6, 9, sit=True)
print(f'\033[30mDicionario: \033[33m{x[0]}!\033[31m\n\033[30mquantidade: \033[33m{x[1]}!\033[30m\n'
      f'\033[30mMaior nota: \033[33m{x[2]}'
      f'!\033[30m\n\033[30mMenor nota:\033[33m {x[3]}!\033[30m\n\033[30mMédia da turma: \033[33m{x[4]}\033[m')
print('\033[m=/' * 15)
