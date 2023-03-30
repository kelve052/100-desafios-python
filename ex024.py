# progama que encontra se o nome comessa com "santo"
cidade = str(input('informe o nome da cidade: ')).strip()
cidade = cidade.upper()
print('\033[33mo nome da cidade comessa com santo?\n\033[32mResposta: {}'.format('SANTO' in cidade[:5]))
