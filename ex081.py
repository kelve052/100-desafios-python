# progama que le valores ate quando o suario decidir parar e mostras as informções
lista = []
while True:
    lista.append(int(input('Digite um valor: [digite 999 para parar!]')))
    if 999 in lista:
        lista.remove(999)
        break
print('-'*43)
print(f'Foram digitados {len(lista)} valores!')
lista.sort(reverse=True)
print(f'A lista em ordem decrecente: {lista}!')
if 5 in lista:
    print('O valor 5 foi digitado e esta na lista!')
else:
    print('O valor 5 não foi digitado e não esta na lista!')