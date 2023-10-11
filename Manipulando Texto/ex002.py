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
n = str(input('Digite um número de 0 á 9999: '))
n.split()                                  # divide a string com numeros
s0 = n[0]                                  # armazena em partes do str
s1 = n[1]
s2 = n[2]
s3 = n[3]
print('unidade: {}'.format(s3))            # Exibe as partes do str
print('dezena: {}'.format(s2))
print('centena: {}'.format(s1))
print('milhar: {}'.format(s0))
