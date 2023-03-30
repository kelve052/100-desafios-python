# fica digitando ate acerta o numero que o computador escolheu (melhora do jogo 28)
import random
palpites = 1
a = int(input('adivinhe um numero de 1 a 5!\n'))
pc = random.randint(1,5)
while a != pc:
    a = int(input('\033[33mtente denovo: '))
    palpites += 1
print(f'\033[32mparabems você adivinhou!\nFoi nessesario {palpites} palpites para voce acerta!')