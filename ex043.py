peso = float(input('digite o peso: '))
altura = float(input('informe a altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('\033[33mAbaixo do peso!')
elif imc < 25:
    print('\033[32mPeso ideal!')
elif imc < 30:
    print('\033[33mSobrepeso!')
elif imc <=40:
    print('\033[31mObesidade!')
else:
    print('\033[35mObesidade Mórbia')