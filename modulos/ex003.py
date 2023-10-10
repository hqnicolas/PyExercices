######################################################################################
#  Script Python escrito em 09/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '19' do curso cursoemvideo.com da aula 8  DESAFIO 019            #
######################################################################################
#  um professor quer sortear um dos seus quatro alunos para apagar o quadro.         #
#  faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido#
######################################################################################
import random                                                      # Importa a biblioteca 'random' para geração de números aleatórios
a1 = input('digite o nome do primeiro aluno: ')                    # Solicita ao usuário que insira o nome do primeiro aluno
a2 = input('digite o nome do segundo aluno: ')                     # Solicita ao usuário que insira o nome do segundo aluno
a3 = input('digite o nome do terceiro aluno: ')                    # Solicita ao usuário que insira o nome do terceiro aluno
a4 = input('digite o nome do quarto aluno: ')                      # Solicita ao usuário que insira o nome do quarto aluno
a = [a1, a2, a3, a4]                                               # Cria uma lista 'a' contendo os nomes dos quatro alunos
print('O Aluno escolhido foi: {}'.format(random.choice(list(a))))  # Imprime o nome do aluno escolhido aleatoriamente
# Escolhe aleatoriamente um aluno da lista 'a' usando 'random.choice'
