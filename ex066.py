# soma varios valores digitados e os soma (valores ilimitados até digitar um comando de parada 999)
b = 0
while True:
    a = int(input('digite um valor --- \033[33m[999 para fechar o progama]: \033[m'))
    if a == 999:
        break
    b = b + a
print('\033[36mA soma de todos os valores digitados foi {}!'.format(b))