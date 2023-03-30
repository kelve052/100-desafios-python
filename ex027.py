# progama que fala qual e o primeiro nome e o ultimo nome de uma pessoa
nome = input('informe um nome completo: ')
nome1 = nome.split()
print('o nome informado "\033[35m{}\033[m"\n o primeiro nome é "\033[36m{}\033[m"\ne o ultimo  nome é "\033[36m{}\033[m"'.format(nome, nome1[0], nome[nome.rfind(' '):]))
