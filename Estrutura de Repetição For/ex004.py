########################################################################################################################
#  Script Python escrito em 19/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 049 laço de Repetição FOR             #
########################################################################################################################
# Refaça o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, so que agora com laço for             #
########################################################################################################################
print('Calculadora de Tabuada')                                    # Apresentação do Script
n = int(input("Digite um número inteiro: "))                       # Solicita ao usuário que insira um número inteiro
for i in range(1, 11):                                             # define um loop em função de "i" de 1 á 10
        r = n * i                                                  # Calcula repetidas vezes o resultado da tabuada
        print("{} x {} = {}" .format(n, i, r))                     # Retorna repetidas vezes o resultado em tela


print('Calculadora de Tabuada')
n = int(input("Digite um número inteiro: "))
for i in range(1, 11):
        print('{} X {:2} = {}'.format(n, i, n*i))
