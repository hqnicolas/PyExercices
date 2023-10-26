########################################################################################################################
#  Script Python escrito em 26/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 054 laço de Repetição FOR             #
########################################################################################################################
# Crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas ainda não atingiram   #
# a maioridade e quantas já são maiores de 21 anos                                                                     #
########################################################################################################################
from datetime import date
h = str(date.today())
s = str(input('em qual ano a {}ª pessoa nasceu? '.format()))
