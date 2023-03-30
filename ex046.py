# progama que fas uma contagem regressiva
from time import sleep
for c in range(10, -1, -1):
    print('\033[37m{}'.format(c))
    sleep(1)
print('\033[32m🎇🎇🎇🎆\033[31m\n🎇🎇🎇🎆\n\033[36m🎇🎇🎇🎆')