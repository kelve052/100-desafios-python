# progama que le o nome e a media de um aluno e a situação e guarda em dicionario
aluno = dict()
aluno['nome'] = str(input('Qual o nome do aluno? '))
aluno['media'] = float(input(f'qual a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = '\033[32mAprovado!\033[m'
elif aluno['media'] >= 5:
    aluno['situação'] = '\033[33mRecuperação!\033[m'
else:
    aluno['situação'] = '\033[31mReprovado!\033[m'
print('-=' * 20)
for i, v in aluno.items():
    print(f'O {i} é igual a {v}')
print('-=' * 20)