######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '11' do curso cursoemvideo.com da aula 7 de operadores           #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==                DESAFIO 009               #
######################################################################################
# um script que leia um numero inteiro qualquer e mostre na tela a sua tabuada       #
######################################################################################
print('Calculadora de Tabuada')                                    # Apresentação do Script
n = int(input("Digite um número inteiro: "))                       # Solicita ao usuário que insira um número inteiro
i = int(0)                                                         # prepara a variável "i" para a execução do while
while (i < 10):                                                    # define um loop em função de "i" de 1 á 10
    i = i + 1                                                      # incrementa o valor de i á cada rodada de while
    r = n * i                                                      # Calcula repetidas vezes o resultado da tabuada
    print("{} x {} = {}" .format(n, i, r))                         # Retorna repetidas vezes o resultado em tela
print('esta é a tabuada de {}' .format(n))                         # Reafirma em tela o numero usado para a tabuada
