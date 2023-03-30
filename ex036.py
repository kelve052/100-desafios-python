# progama ve se se da pra voce financiar uma casa e acordo com seu salario e calcula quantas parcelas dependendo o ano
casa = float(input('qual o valor da casa á financiar: '))
salario = float(input('qual seu salario: '))
sa30 = (salario*30/100)
anos = int(input('em quantos anos ira pagar o financiamneto: '))
prestacao = casa/(anos*12)
if prestacao >sa30:
    print('\033[31minfelizmnete a parcela da casa exedeu \033[35m30%\033[m \033[31mdo seu salario, não será possivel financear a casa!')
else:
    print(sa30, '\n\033[32mparabem você poderá financear a casa!\033[m\npagando uma parcela por mês no valor de \033[32mR${:.2f}\033[32m\nem \033[35m{} anos'.format(prestacao, anos))