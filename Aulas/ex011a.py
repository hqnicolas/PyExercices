######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '11' do curso cursoemvideo.com da aula 7 de operadores           #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==                                          #
######################################################################################
# um script que leia um numero inteiro qualquer e mostre na tela a sua tabuada       #
######################################################################################
print('Calculadora de Tabuada')                                    # Apresentação do Script
n = int(input("Digite um número inteiro: "))                       # Solicita ao usuário que insira um número inteiro
r = n * 1                                                          # Calcula a tabuada
print('{} X 1 = {}'.format(n, r))                                  # Exibe a tabuada
r = n * 2
print('{} X 2 = {}'.format(n, r))
r = n * 3
print('{} X 3 = {}'.format(n, r))
r = n * 4
print('{} X 4 = {}'.format(n, r))
r = n * 5
print('{} X 5 = {}'.format(n, r))
r = n * 6
print('{} X 6 = {}'.format(n, r))
r = n * 7
print('{} X 7 = {}'.format(n, r))
r = n * 8
print('{} X 8 = {}'.format(n, r))
r = n * 9
print('{} X 9 = {}'.format(n, r))
r = n * 10
print('{} X 10 = {}'.format(n, r))
print('esta é a tabuada de {}' .format(n))                          # Reafirma em tela o numero usado para a tabuada

