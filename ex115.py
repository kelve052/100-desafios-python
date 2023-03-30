# progama que cadrasta pessoas e salva em um arquivo de texto usando modulo
# na resolução do ex115b ele ensima comandos amais sobre arquivos txt. Link: https://youtu.be/bfTFe6bKLXk
from time import sleep

nome = ''
idade = 0
lista = list()
exe = 0

print('\t\t\t\t\t\033[1:34:43m===Lista de Pessoas===\033[m')
while exe == 0:

    for c in range(1, 48):
        sleep(0.01)
        print('\033[m-', end='')
    print()
    print('\033[32m1 - Ver lista de cadastro!\n'
            '2 - Adicionar pessoa na lista!\n'
            '3 - fechar progama\033[m')
    print('-' * 47)

    try:
        while True:
            op = int(input('---'))
            if op == 1:
                with open('cadastro de pessoas.txt', 'r') as arquivo:
                    exibir = arquivo.readlines()
                    print('-' * 47)
                    print(f'\033[1:34m{"nome":<21}Idade\033[0:33m')
                    for c in range(1, len(exibir) + 1):
                        sleep(0.5)
                        print(exibir[c - 1], end='')
                    break
            elif op == 2:
                nome = input('\033[33mDigite o nome da pessoa: ')
                with open('cadastro de pessoas.txt', 'a') as arquivo:
                    arquivo.write(f'{nome:-<24}')
                while True:
                    idade = (input('digite a idade da pessoa: '))
                    if idade.isnumeric() == True:
                        with open('cadastro de pessoas.txt', 'a') as arquivo:
                            arquivo.write(idade + '\n')
                        break
                break
            elif op == 3:
                print('-' * 60)
                print('\t\t\t\t\t\033[1:34:43m===Processo finalizado===\033[m')
                exe = 1
                break
            else:
                print('\033[31mDigite uma opição valida!(1, 2, 3)\033[m')
    except ValueError:
        print('\033[31mDigite uma opição valida!\033[m')


