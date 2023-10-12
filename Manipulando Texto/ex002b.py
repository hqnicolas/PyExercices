######################################################################################
#  Script Python escrito em 10/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com desafio 23 da manipulação de cadeias de texto   #
######################################################################################
# leia um numero de 0 á 9999 e mostre na tela os digitos separados.                  #
# Ex: Digite um número: 1834                                                         #
# unidade: 4                                                                         #
# dezena: 3                                                                          #
# centena: 8                                                                         #
# milhar: 1                                                                          #
######################################################################################
n = int(input('Digite um número de 0 á 9999: '))   # Solicita ao usuário que digite um número de 0 a 9999 e armazena a entrada em 'n'
s0 = n // 1 % 10                                   # Calcula e armazena a unidade (dígito mais à direita) do número
s1 = n // 10 % 10                                  # Calcula e armazena a dezena (segundo dígito da direita) do número
s2 = n // 100 % 10                                 # Calcula e armazena a centena (terceiro dígito da direita) do número
s3 = n // 1000 % 10                                # Calcula e armazena o milhar (quarto dígito da direita) do número
print('unidade: {}'.format(s0))                    # Imprime a unidade
print('dezena: {}'.format(s1))                     # a dezena
print('centena: {}'.format(s2))                    # a centena
print('milhar: {}'.format(s3))                     # o milhar do número
