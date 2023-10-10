######################################################################################
#  Script Python escrito em 09/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '18' do curso cursoemvideo.com da aula 8  DESAFIO 018            #
######################################################################################
#  Faça um programa que leia um angulo qualquer e mosrte                             #
#  na tela o valor do seno cosseno e tangente desse angulo                           #
######################################################################################
import math                                  # Importa a biblioteca 'math' para usar funções matemáticas
a = float(input('digite um ângulo: '))       # Solicita ao usuário que insira um ângulo
t = math.tan(math.radians(a))                # Calcula o seno do ângulo usando a função 'math.sin'
s = math.sin(math.radians(a))                # Calcula o cosseno do ângulo usando a função 'math.cos'
c = math.cos(math.radians(a))                # Calcula a tangente do ângulo usando a função 'math.tan'
print('\nSeno: {:.2f} \ncosseno: {:.2f} \ntangente: {:.2f}'.format(s, c, t))
# Imprime os valores do seno, cosseno e tangente formatados com duas casas decimais
