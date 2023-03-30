# progama serva pra ver se tem o nome "silva" em alguma parte do nome
nome = input('informe um nome: ')
nome1 = nome.upper()
print('o nome \033[34m{} tem o nome \033[1;30m"silva"\033[m em alguma parte\n\033[36mResposta: {}'.format(nome, ' SILVA ' in nome1))
