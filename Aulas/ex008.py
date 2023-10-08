######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '8' do curso cursoemvideo.com                                    #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==                                          #
######################################################################################
# faça um programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada   #
######################################################################################
print('Exibir Dobro, triplo e Raiz ')                            # Print em tela da descrição do script
n1 = int(input('Digite um número inteiro: '))                    # Solicita ao usuário um número inteiro
nr = n1 ** (0.5)
nd = n1 * 2
nt = n1 * 3
if nr % 1 == 0:                                                  # Verifica se a parte decimal é zero
    ni = int(nr)                                                 # Se a parte decimal for zero, converte para int
    print('a raiz de {} é {}' .format(n1, ni))                   # Se a parte decimal for zero, exibe o "ni" int
else:
    print('a raiz de {} é {}' .format(n1, nr))                   # Se a parte decimal não for zero exibe "nr" float
print('o dobro de {} é {}' .format(n1, nd))                      # Exibe o dobro
print('o triplo de {} é {}' .format(n1, nt))                      # Exibe o triplo
