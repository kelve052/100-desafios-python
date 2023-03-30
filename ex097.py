# progama que usa uma função que dependendo do tamnhanho da palavra as linhas se adapitao
def escreva(text):
    a = len(text)
    print('-' * a)
    print(text)
    print('-' * a)


escreva('barbearia')
escreva('marca')
escreva('Otoringolarindologista')