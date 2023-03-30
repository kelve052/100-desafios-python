# progama que mostra a sequencia de fibonacci
a = int(input('\033[34mdigite qauntos termos deseja mostrar do fibonancci: '))
cont = 3
t1 = 0
t2 = 1
print(t1, ' -> ', t2, end='\033[34m -> \033[m',)
while cont <= a:
    cont += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end=' -> ')
