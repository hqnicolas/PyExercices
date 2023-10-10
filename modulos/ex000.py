######################################################################################
#  Script Python escrito em 09/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '16' do curso cursoemvideo.com da aula 8  DESAFIO 016            #
######################################################################################
#  Crie um Programa que leia um numero real qualquer                                 #
#  pelo teclado e mostre na tela a sua porção inteira                                #
######################################################################################
import math                                         # Importa a biblioteca 'math' para usar funções matemáticas
num = float(input('Digite um número quebrado: '))   # Solicita ao usuário que insira um número quebrado e o converte para ponto flutuante
c = math.ceil(num)                                  # Usa a função 'math.ceil' para arredondar para cima e obter a próxima parte inteira
t = math.trunc(num)                                 # Usa a função 'math.trunc' para arredondar para baixo e obter a parte inteira do número
print('A porção inteira de {} é o numero: {} e a não inteira: {}'.format(num, t, c))
# Imprime a porção inteira e não inteira do número na tela
