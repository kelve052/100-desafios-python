import random
aluno1 = input('informe o primeiro aluno: ')
aluno2 = input('informe o segundo aluno: ')
aluno3 = input('informe o terceiro aluno: ')
aluno4 = input('informe o quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('o alunos escolhido foi: \033[33m', escolhido)
