# progama que verifica se um site esta diponivel ou não (não consegui faser e tive que olhar a solução,
# mas tentei pesquisar antes e vi algo semelhante ao do video
# não resolvido pois no video esta desuatualizado

import urllib
import urllib.request

try:
    site = urllib.request('http://www.pudim.com.br/')
except:
    print('deu erro')
else:
    print('deu certo')