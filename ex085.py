# progama que le 7 valores e separa em duas listaa imprar e par dentro de uma lista unica
impar = []
par = []
valores = [[], []]
for c in range(1, 8):
    p = int(input(f'{c}° valor: '))
    if p % 2 == 0:
        valores[1].append(p)
    else:
        valores[0].append(p)
valores[1].sort()
valores[0].sort()
print(f'Os valores impares são: {valores[0]}\nOs valores pares são: {valores[1]}')