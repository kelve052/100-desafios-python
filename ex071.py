# progama que simula um caixa eletronico e o valor sacado sai quantas notas sairam.
# (no exercicio 71 o cara do video fas de uma maneira em que se as notas forem 0 elas não apraressem)
valor = int(input('\033[36mdigite o valor a ser sacado: \033[m'))
valor1 = valor
c50 = 0
c20 = 0
c10 = 0
c1 = 0
while valor >= 50:
    valor = valor - 50
    c50 = c50 + 1
while valor >= 20:
    valor = valor - 20
    c20 = c20 + 1
while valor >= 10:
    valor = valor - 10
    c10 = c10 + 1
while valor >= 1:
    valor = valor - 1
    c1 = c1 + 1
print(f'O valor sacado foi de \033[32m{valor1}\n\033[35m {c50} notas de R$50!\n{c20} notas de R$20!\n{c10} notas de '
      f'R$10!\n{c1} moedas de R$1!')
