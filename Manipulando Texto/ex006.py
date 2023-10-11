######################################################################################
#  Script Python escrito em 11/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com desafio 26 da manipulação de cadeias de texto   #
######################################################################################
# Faça um programa que leia o nome completo de uma pesso, mostrando em seguida       #
# o primeiro e o ultimo nome separadamente.                                          #
# Ex: Ana Maria de Souza                                                             #
# Primeiro = Ana                                                                     #
# Ultimo = Souza                                                                     #
######################################################################################
i = input('Digite o nome completo: ')                     # Solicita ao usuário que digite um nome completo e armazena a entrada em 'i'
print('que nome grande!\n vamos abreviar...')
n = i.split()                                             # Divide o nome completo em palavras separadas com base nos espaços em branco
print('Primeiro: {} \n Ultimo: {}'.format(n[0], n[-1]))   # Imprime o primeiro nome (primeiro elemento da lista) e o último nome (último elemento da lista)
