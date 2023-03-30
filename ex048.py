# progama que le todos os numeros impares de 1 a 500 e multiplos de 3 e da a soma desses numeros
soma = 0
valores = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        valores = valores + 1
        soma = soma + c
print('A soma de todos os numeros \033[35mimpares\033[m e \033[35mmultiplos\033[m de 3 é \033[34m', soma, '\033[me o total de valores foi\033[32m', valores)