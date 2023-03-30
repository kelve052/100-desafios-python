# tupla com os 20 primeioros livros da biblia mostrando informações
tupla = ('Gênesis', 'Êxodo', 'Levítico', 'Números', 'Deuteronômio', 'Josué', 'Juíses', 'Rute', '1Samuel', '2Samuel',
'1Reis', '2REIS', '1Crônicas', '2Crônicas', 'Esdras', 'Neemias', 'Ester', 'Jó', 'Salmos', 'Provérbios')
a = tupla.index('Provérbios')
print(f'\033[36mos 5 primeiros livros da biblia é {tupla[0:6]}!\nOs quatros ultimos são {tupla[16:]}!')
print(f'E o livro de Porvérbios esta na posição {a}!')
print(f'os 20 primeiros livros da Biblia em ordem alfabética é: \033[33m{sorted(tupla)}')
