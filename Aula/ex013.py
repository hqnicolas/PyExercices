######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '13' do curso cursoemvideo.com da aula 7  DESAFIO 011            #
######################################################################################
#  Faça um programa que leia a largura e a altura de uma parede em metros, calcule   #
#  a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada     #
#  litro de tinta pinta uma área de 2 metros quadrados.                              #
######################################################################################
l = float(input('Qual a largura da parede?: '))                                                # a variável "l" recebe o valor de largura
a = float(input('Qual a altura da parede?: '))                                                 # a variável "a# " recebe o valor de altura
q = l * a                                                                                      # "q" recebe o valor da área
print('Sua parede tem dimensões de {:.1f}x{:.1f}m e sua área é de {:.2f}m²' .format(l, a, q))  # o terminal exibe o valor de área "q"
l = q / 2                                                                                      # "l" recebe o valor de litros de tinta
print('Para pintar essa parede você precisará de {:.2f}l de tinta.'.format(l))                 # o terminal exibe o valor de litros de tinta
