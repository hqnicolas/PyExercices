########################################################################################################################
#  Script Python escrito em 15/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 42 condições e Repetições de codigo              #
########################################################################################################################
# Refaça o desafio 35 dos triangulos acrecentando o recurso de mostrar que tipo de triangulo será formado:             #
# - Equilátero: Todos os lados iguais                                                                                  #
# - Isósceles: dois lados iguais                                                                                       #
# - Escaleno: Todos os lados diferentes                                                                                #
########################################################################################################################
print('Digite os três lado do Triangulo')                            # Solicita ao usuário que insira os três lados do triângulo
a = float(input('lado a: '))
b = float(input('lado b: '))
c = float(input('lado c: '))
if a + b <= c or c + b <= a or a + c <= b:                              # Verifica se é possível formar um triângulo com os lados fornecidos
    print('!Este triangulo não é possível!')
else:
    print('Podemos chamar de triangulo {:.1f} - {:.1f} - {:.1f}'.format(a, b, c))
    if a == b == c:
        print('****** Equilatero! ******')                           # EQUILÁTERO se todos os lados iguais
    elif a == b != c or a == c != b or b == c != a:
        print('****** Isósceles! ******')                            # ISÓSCELES se dois lados iguais, um diferente
    elif a != b != c:
        print('****** Escaleno! ******')                             # ESCALENO se todos os lados diferentes
