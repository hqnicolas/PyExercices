######################################################################################
#  Script Python escrito em 10/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com desafio 22 da manipulação de cadeias de texto   #
######################################################################################
# Crie um programa que leia o nome completo de uma pessoa e mostre:                  #
# O nome com todas as letras maiúsculas                                              #
# O nome com todas as letras minúsculas                                              #
# Quantas letras total sem considerar espaços                                        #
# Quantas letras tem o primeiro nome                                                 #
######################################################################################
nome = input('Digite o seu nome completo: ')                        # Solicita ao usuário que insira o nome completo
print(nome.lower())                                                 # Converte o nome para letras minúsculas e imprime
print(nome.upper())                                                 # Converte o nome para letras maiúsculas e imprime
space = nome.count(' ')                                             # Conta os espaços no nome para determinar o número de palavras
count = len(nome)                                                   # (presumindo que o nome seja composto por palavras separadas por espaços)
t = count - space                                                   # Calcula o comprimento total do nome, subtraindo os espaços
print('O nome: {} tem {} letras!'.format(nome, t))                  # Exibe o nome e o número total de letras
s = nome.split()                                                    # Divide o nome em palavras
s0 = s[0]                                                           # pega o primeiro nome
print('O Primeiro nome: {} tem {} letras!'.format(s0, len(s0)))     # Exibe o primeiro nome e seu comprimento
