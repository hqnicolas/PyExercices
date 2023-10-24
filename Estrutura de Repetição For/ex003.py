########################################################################################################################
#  Script Python escrito em 19/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 048 laço de Repetição FOR             #
########################################################################################################################
# Crie um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no      #
# intervalo de 1 até 500                                                                                               #
########################################################################################################################
print('Multiplos de 3, entre 1 - 500')                      # Imprime um cabeçalho para indicar o que o programa faz
s = 0                                                       # Inicializa uma variável para armazenar a soma dos números ímpares que são múltiplos de 3
for i in range(1, 501):                                     # Loop for que percorre os números de 1 a 500
    if i % 3 == 0 and i % 2 == 1:
        s += i
print('{}'.format(s))                                       # Imprime a soma formatada como uma string
