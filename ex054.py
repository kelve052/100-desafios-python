# progama que le datas de nacimento e fala quais são maiores de idade
import datetime
p1 = int(input('informe a data de nacimento da 1° pessoa: '))
p2 = int(input('informe a data de nacimento da 2° pessoa: '))
p3 = int(input('informe a data de nacimento da 3° pessoa: '))
p4 = int(input('informe a data de nacimento da 4° pessoa: '))
p5 = int(input('informe a data de nacimento da 5° pessoa: '))
p6 = int(input('informe a data de nacimento da 6° pessoa: '))
p7 = int(input('informe a data de nacimento da 7° pessoa: '))
lista = [p1, p2, p3, p4, p5, p6, p7]
tot = 0
tot2 = 0
ano = datetime.date.today().year
for a in range(0, 7):
    if ano - lista[a] <21:
        tot += 1
    else:
        tot2 += 1
print('\033[34mHá {} pessoas maiores de idade!\n\033[36mE há {} menores de idade!'. format(tot2, tot))