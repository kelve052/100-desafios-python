import math
a = int(input('informe o angulo: '))
rad = a*3.14/180
sen = math.sin(rad)
tang = math.tan(rad)
cos = math.cos(rad)
print(' de acordo com o angulo informado {}\n\033[35mo seno é {:.2f}\n\033[33mo coseno é {:.2f} \n\033[34me a tang é {:.2f}'.format(a, sen, cos, tang))
