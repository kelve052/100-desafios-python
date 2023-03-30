# progama que le o tamanho de tres retas e verifica se da pra formar um triangulo
r1 = float(input('informe o tamanho da primeira reta em metros: '))
r2 = float(input('informe o tamanho da segunda reta: '))
r3 = float(input('informe o tamnho da terceira reta: '))
if (r1+r2)>r3>(r1-r2) and (r2+r3)>r1>(r2-r3) and (r1+r3)>r2>(r1-r3):
    print('com as retas infomadas:\n\033[35mr1 = {}m\nr2 = {}m\nr3 = {}m\n\033[mé \033[36mSIM\033[m possivel formar um \033[36mtriangulo!'.format(r1, r2, r3))
else:
    print('com as retas infomadas:\033[35m\nr1 = {}m\nr2 = {}m\nr3 = {}m\n\033[31mNÃO\033[m é possivel formar um \033[31mtriangulo!'.format(r1, r2, r3))