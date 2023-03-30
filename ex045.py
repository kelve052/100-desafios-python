# jogo de jokempo com o computador
voce = input('\033[33mPedra\n\033[34mPapél\n\033[36mTesoura\033[m\n').strip().upper()
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
lista = [pedra, papel, tesoura]
import random
pc = random.choice(lista)
if pc == voce:
    print('\033[33mEmpate!')
elif pc == pedra and voce == tesoura:
    print('PC escolheu \033[36mpedra\033[m e voce escolheu \033[36mtesoura\n\033[31mVoce perdeu!')
elif pc == tesoura and voce == pedra:
    print('PC escolheu \033[36mtesoura\033[m e voce escolheu \033[36mpedra\n \033[32mvoce ganhou!')
elif pc == papel and voce == pedra:
    print('PC escolheu \033[36mpapel\033[m e voce \033[36mpedra\n \033[31mvoce perdeu!')
elif pc == pedra and voce == papel:
    print('PC escolheu \033[36mpedra\033[m e voce escolheu \033[36mpapel\n \033[32mvoce ganhou!')
elif pc == tesoura and voce == papel:
    print('PC escolheu \033[36mtesoura\033[m e voce escolheu \033[36mpapel \n \033[31mvoce perdeu!')
elif pc == papel and voce == tesoura:
    print('PC escolheu \033[36mpapel\033[m e voce escolheu \033[36mtesoura\n \033[32mvoce ganhou!')
else:
    print('\033[31mvoce escolheu uma opição invalidada do jokempo!')