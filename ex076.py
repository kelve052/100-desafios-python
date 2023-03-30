# prgama que mostra nome e presso do profuo em uma unica tupla e bem formatado o print
tupla = ('manteiga', 4.50, 'maçã', 1.45, 'sorvete', 7, 'picole',
1.15, 'refrigerante', 5, 'pipino', 7.55, 'suco', 50, 'yorgute', 5.40)
for c in range(0, (len(tupla))+1, 2):
    print(f'\033[33m {tupla[c]:.<30} \033[30m \033[32mR${tupla[c+1]}')