######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '4' do curso cursoemvideo.com                                    #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==                                          #
######################################################################################
#   5 + 2 == 7                                                                       #
#   5 - 2 == 3                                                                       #
#   5 * 2 == 10                                                                      #
#   5 / 2 == 2.5                                                                     #
#   5 ** 2 == 25                                                                     #
#   5 // 2 == 2                                                                      #
#   5 % 2 == 1                                                                       #
######################################################################################
#   Ordem de Precedência                                                             #
#   ()       Parenteses                                                              #
#   **       Exponênciação                                                           #
#   * / // % Multiplicação, divisão, divisão inteira e resto da divisão              #
#   + -      Soma e subitração binária                                               #
######################################################################################
# leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor            #
######################################################################################
print('Exibir Sucessor e Antecessor ')             # Print em tela da descrição do script
n1 = int(input('Digite um número inteiro: '))      # Solicita ao usuário um número inteiro
n2 = n1 + 1                                        # Calcula o sucessor e o antecessor
n0 = n1 - 1
print('O sucessor de {} é {}.' .format(n1, n2))    # Exibe os resultados
print('O antecessor de {} é {}.' .format(n1, n0))
