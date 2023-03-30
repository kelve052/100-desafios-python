# progama que le dois valores e manda voce escolher a o que voce quer faser e se quer continuar
r = 0
n1 = int(input('informe o primeiro valor: '))
n2 = int(input('informe o segundo valor: '))
while r != 5:
    op = int(input('qual operação deseja realizar com os dois valores?\n\033[35m1 - [somar]\n2 - [multiplicar]\n3 - [maior]\n4 - [novos valores]\n5 - [fechar progama]\033[m'))
    if op == 1:
        res = n1 + n2
        print('a soma dos dois valores é {}'.format(res))
    elif op == 2:
        res = n1 * n2
        print('a multiplicaçõ dos dois valores é: {}'.format(res))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('dos dois valores informados o maior é {}'.format(maior))
    elif op == 4:
        print('\033[32mtroque os valores!')
        n1 = int(input('informe o primeiro valor: '))
        n2 = int(input('informe o segundo valor: '))
    elif op == 5:
        r = 5
    else:
        print('\033[31mopição invalida!\033[m')
print('\033[35moperação finalizada!')
