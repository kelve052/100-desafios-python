n1 = float(input('informe a primeira nota: '))
n2 = float(input('informe a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('\033[32maprovado!')
elif 5 <= media < 7:
    print('\033[33mRecuperação!')
else:
    print('\033[31mReprovado!')