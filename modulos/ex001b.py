######################################################################################
#  Script Python escrito em 09/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '17' do curso cursoemvideo.com da aula 8  DESAFIO 017            #
######################################################################################
#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjaceite    #
#  de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa           #
######################################################################################
from math import sqrt                                    # Importa somente sqrt da biblioteca math
c = float(input('Digite o cateto oposto: '))              # Solicita ao usuário que insira o valor do cateto oposto e o converte para ponto flutuante
b = float(input('Digite o cateto adjacente: '))           # Solicita ao usuário que insira o valor do cateto adjacente e o converte para ponto flutuante
print('A hipotenusa é: {:.2f}'.format(sqrt(c*c + b*b)))   # Calcula a hipotenusa diretamente usando o teorema de Pitágoras (a² = b² + c²) e math.sqrt para encontrar a raiz quadrada
