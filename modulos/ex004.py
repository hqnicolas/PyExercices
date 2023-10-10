######################################################################################
#  Script Python escrito em 09/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '20' do curso cursoemvideo.com da aula 8  DESAFIO 020            #
######################################################################################
#  o mesmo professor do desafio anterior quer sortear a ordem de apresentação        #
#  de trabalhos dos alunos faça um programa que leia o nome                          #
#  dos quatro alunos e mostre a ordem sorteada                                       #
######################################################################################
import random                                         # Importa a biblioteca 'random' para geração de números aleatórios
a1 = input('digite o nome do aluno 1: ')              # Solicita ao usuário que insira o nome do aluno 1
a2 = input('digite o nome do aluno 2: ')              # Solicita ao usuário que insira o nome do aluno 2
a3 = input('digite o nome do aluno 3: ')              # Solicita ao usuário que insira o nome do aluno 3
a4 = input('digite o nome do aluno 4: ')              # Solicita ao usuário que insira o nome do aluno 4
a = [a1, a2, a3, a4]                                  # Cria uma lista 'a' contendo os nomes dos quatro alunos
random.shuffle(a)                                     # Embaralha aleatoriamente a ordem dos nomes na lista 'a' usando 'random.shuffle'
print('A sequência de apresentação é: {}'.format(a))  # Imprime a sequência sorteada de apresentação
