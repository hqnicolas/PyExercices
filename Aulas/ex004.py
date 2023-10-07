######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '4' do curso cursoemvideo.com                                    #
#  crie um programa que leia dois numeros e mostre a soma entre eles                 #
######################################################################################
print('Calculadora de Soma')                              # Print em tela da descrição do script
n1 = int(input('Digite o primeiro número: '))             # Input recebe o valor para "n1"
n2 = int(input('Digite o segundo número: '))              # Input recebe o valor para "n2"
s = n1 + n2                                               # Soma os valores de duas variáveis int
print('A soma de {} com {} é: {}'.format(n1, n2, s))      # exibe na tela o resultado da soma
