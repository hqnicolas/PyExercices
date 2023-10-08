######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '8' do curso cursoemvideo.com     DESAFIO 006                    #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==                                          #
######################################################################################
# faça um programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada   #
######################################################################################
print('Exibir Dobro, triplo e Raiz ')                            # Print em tela da descrição do script
n = int(input('Digite um número inteiro: '))                    # Solicita ao usuário um número inteiro
print('O dobro de {} vale {}.' .format(n, (n*2)))
print('O Triplo de {} vale {}, \nA raiz quadrada de {} é igual a {:.2f}.' .format(n, (n*3), n, pow(n, (1/2))))
