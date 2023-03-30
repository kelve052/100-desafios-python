# prgama que calcula a PA ate 10
p = int(input('informe o primeiro termo da PA: '))
r = int(input('informe a razão da PA: '))
b = 0
c = 0
ras = p + (10 - 1)* r
for v in range(p, ras + r, r):
    b = v
    print(b)
