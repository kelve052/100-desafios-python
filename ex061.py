# prgama que calcula a PA ate 10 (usando whiler sendo que o 51 foi usando for)
p = int(input('informe o primeiro termo da PA: '))
r = int(input('informe a razão: '))
cont = 1
while cont != 11:
    print(p)
    p = p + r
    cont += 1