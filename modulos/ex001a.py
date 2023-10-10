######################################################################################
#  Script Python escrito em 09/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '17' do curso cursoemvideo.com da aula 8  DESAFIO 017            #
######################################################################################
#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjaceite    #
#  de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa           #
######################################################################################
import math                                              # Importa a biblioteca 'math' para usar funções matemáticas
c = float(input('Digite o cateto oposto: '))             # Solicita ao usuário que insira o valor do cateto oposto e o converte para ponto flutuante
b = float(input('Digite o cateto adjacente: '))          # Solicita ao usuário que insira o valor do cateto adjacente e o converte para ponto flutuante
c2 = math.pow(c, 2)                                      # Calcula o quadrado do cateto oposto usando math.pow
b2 = math.pow(b, 2)                                      # Calcula o quadrado do cateto adjacente usando math.pow
a2 = b2 + c2                                             # Calcula o quadrado da hipotenusa usando o teorema de Pitágoras (a² = b² + c²)
a = math.sqrt(a2)                                        # Calcula a hipotenusa tomando a raiz quadrada do quadrado da hipotenusa
print('A hipotenusa é: {:.2f}'.format(a))                # Imprime a hipotenusa na tela
