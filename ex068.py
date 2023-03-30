# jogo pedra papel e tesoura (usando while e break)
import random
cont = 0
while True:
    eu = int(input('\033[30mDigite um valor: '))
    esc = str(input('\033[36mPAR -> [P] \033[mou \033[34mIMPAR -> [I]')).upper()
    pc = random.randint(0, 10)
    res = pc + eu
    if res % 2 == 0:
        if eu == 'p':
            print('\033[32mVoce venceu!')
            cont = cont + 1
        else:
            print('\033[30m=================\n\033[33mvoce perdeu!\n\033[34mvoce venceu {} veses\033[30m\n================='.format(cont))
            break
    else:
        if eu == 'p':
            print('\033[30m=================\n\033[33mvoce perdeu!\n\033[34mvoce venceu {} veses\033[30m\n================='.format(cont))
            break
        else:
            print('\033[32mVoce venceu!')
            cont = cont + 1


