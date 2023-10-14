########################################################################################################################
#  Script Python escrito em 13/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 37 condições e Repetições de codigo              #
########################################################################################################################
# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de converção #
# 1 para binário                                                                                                       #
# 2 para Octal                                                                                                         #
# 3 para hexadecimal                                                                                                   #
########################################################################################################################
n = int(input('* Digite um número inteiro: '))
o = int(input('* Qual será a base de conversão?\n* Digite 1 para Binário.\n* Digite 2 para Octal.\n* Digite 3 para Hexadecimal: '))
if o == 1:
    print('* O valor {} em binário é: {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('* O valor {} em Octal é: {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('* O valor {} em binário é: {}'.format(n, hex(n)[2:]))

#######################################################################
# [2:] exibe á partir do segundo caractere da variável string
# usando o método de fatiamento de string da aula 10
# removendo assim o "0b" do binário, "0x" do Hexadecimal e "0o" do octal.
#######################################################################
# função oct() padrão do python converte a variável n em octal
# função bin() padrão do python converte a variável n em binário
# função hex() padrão do python converte a variável n em hexadecimal
