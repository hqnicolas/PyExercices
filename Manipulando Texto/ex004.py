######################################################################################
#  Script Python escrito em 11/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com desafio 25 da manipulação de cadeias de texto   #
######################################################################################
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome   #
######################################################################################
i = input('Digite seu nome: ')                    #Solicita ao usuário digitar o nome
n = i.lower().strip()                             #Converte a frase para letras minúsculas (para não diferenciar maiúsculas de minúsculas)
s = n.count('silva')                              #verifica a presença de silva no nome
print('O nome {}, contém {} silva'.format(n, s))  #Exibe o resultado da verificação
