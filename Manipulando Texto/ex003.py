######################################################################################
#  Script Python escrito em 10/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com desafio 24 da manipulação de cadeias de texto   #
######################################################################################
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome#
#                                      "santo"                                       #
######################################################################################
nome = input('digite o nome de uma cidade: ')                    # Solicita ao usuário que insira o nome de uma cidade
divide = nome.lower().split()                                    # Divide o nome da cidade em palavras,
primeiro = divide[0]                                             #  converte para letras minúsculas e pega a primeira palavra
if 'santo' == primeiro:                                          # Verifica se a primeira palavra é "santo" ou "santa"
    print('A cidade {} começa com santo'.format(nome))
else:
    if 'santa' == primeiro:
        print('A cidade {} começa com santa'.format(nome))
    else:
        print('A cidade {} não começa com santo'.format(nome))
