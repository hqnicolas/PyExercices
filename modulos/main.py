##########################################################################
# Bibliotecas                                                            #
# https://docs.python.org/3.12/library/index.html                        #
# exemplos                                                               #
##########################################################################
# biblioteca: math                                                       #
# comandos da biblioteca: Ceil, floor, trunc, pow, sqrt, factorial       #
# importação completa:                                                   #
# import math                                                            #
##########################################################################
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
##########################################################################
# importação otimizada de funcionalidade:                                #
# from math import sqrt                                                  #
##########################################################################
from math import sqrt
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
##########################################################################
