# progama que le 4 valores e os guarda em uma tupla e mostra a analize da tupla
a = int(input('\033[33:40mDigite primeiro valor: \033[m'))
b = int(input('\033[33:40mDigite segundo valor: \033[m'))
c = int(input('\033[33:40mDigite terceiro valor: \033[m'))
d = int(input('\033[33:40mDigite quarto valor: \033[m'))
numeros = (a, b, c, d)
print(f'\033[34mO numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 foi digitado na posição {(numeros.index(3))+1}!')
print(f'Os numeros pares foram ', end=' \033[32m')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
