co = float(input('informe o cateto oposto: '))
ca = float(input('informe o cateto adijacente: '))
import math
h = math.hypot(co, ca)
print('a \033[31mhipotenza\033[m do triangulo é \033[31m{:.2f} '.format(h))

