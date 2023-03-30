# progama testa se o ano é bisesto ou não
ano = int(input('gitite um ano, ou 0 para analizar o ano atual: '))
import datetime
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano \033[34m{}\033[m é \033[33mbixesto'.format(ano))
else:
    print('o ano \033[34m{} \033[31mnão é bixesto'.format(ano))
