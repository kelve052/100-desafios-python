aluno1 = input('informe o primeiro aluno: ')
aluno2 = input('informe o segundo aluno: ')
aluno3 = input('informe o terceiro aluno: ')
aluno4 = input('informe o quarto aluno: ')
lista1 = [aluno1, aluno2, aluno3, aluno4]
import random
random.shuffle(lista1)
print('a ordem é escohida foi: \033[35m', lista1)
