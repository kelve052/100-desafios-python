idade = int(input('qual a a data de nacimento do atetla: '))
import datetime
ano = datetime.date.today().year
idade = ano - idade
if idade < 10:
    print('A idade do atléta é {}\nclassificação: Mirim!'.format(idade))
elif idade < 15:
    print('A idade do atléta é {}\nclassificação: Infantil!'.format(idade))
elif idade < 20:
    print('A idade do atléta é {}\nclassificação: Junior!'.format(idade))
elif idade == 20:
    print('A idade do atléta é {}\nclassificação: Sênior!'.format(idade))
else:
    print('A idade do atléta é {}\nclassificação: Master'.format(idade))