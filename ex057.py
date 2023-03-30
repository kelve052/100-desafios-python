# progama que fica repetindo ate voce digitar um sexo valido
a = str(input('qual seu sexo? ')).upper()
while a not in 'FM':
    a = str(input('\033[31mSexo invalido!\n\033[mqual seu sexo? ')).upper()
print('\033[36msexo registrado!')

