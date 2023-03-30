# progama que um numero digitado ele informa o a versão do numero em escrita emtre 0 e 20
tupla = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Trese', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Desoito', 'Dezenove', 'Vinte')
while True:
    op = int(input('\033[30mDigite um numero entre 0 e 20: '))
    if op >= 0 and op < 21:
        break
print(f'\033[33mO valor digitado foi {op}! Escripor por extenso esse valor é \033[33:40m{tupla[op]}!\033[m')