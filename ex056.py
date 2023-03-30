#progama que analiza o nome
print('Informe a idade nome e sexso de tres pessoas: ')
idade1 = 0
idadev = 0
mulheres = 0
velhor = ''
for a in range(1, 5):
    nome = input('\033[34mNome: ')
    idade = int(input('\033[34mIdade: '))
    sexo = input('\033[34msexo\033[33m(F/M)\033[34m:').strip().upper()
    print('\033[30m=============================================')
    idade1 += idade
    if idade > idadev and sexo == 'M':
        idadev = idade
        velhor = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('\033[33mA média da idade do grupo é \033[35m{}'.format(idade1/4))
print('\033[33mO homem mais velhos se chama \033[35m{}'.format(velhor))
print('\033[33mo total de mulheres com menos de 20 anos é \033[35m{}'.format(mulheres))
