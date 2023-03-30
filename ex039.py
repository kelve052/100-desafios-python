idade = int(input('informe a data de nacimento: '))
import datetime
falta = datetime.date.today().year
if falta - idade == 18:
    print('\033[32mesta na hora de se alistar!')
elif falta - idade < 18:
    falta2 = 18 - (falta - idade)
    falta = falta + falta2
    print('\033[33mainda não esta na hora de se alistar!\n\033[34mAinda falta {} anos para se alistar!\n\033[34me seu alistamento sera em {}'.format(falta2, falta))
else:
    falta2 = (falta - idade) - 18
    falta = falta - falta2
    print('\033[31mja passou da hora de se alistar!\n\033[34mJa passou {} anos para se apresentar!\n\033[34mseu alistamento foi em {}'.format(falta2, falta))