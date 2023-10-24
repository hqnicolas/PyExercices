########################################################################################################################
#  Script Python escrito em 19/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 046 laço de Repetição FOR             #
########################################################################################################################
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio indo de 10 até 0    #
# com uma pausa de 1 segundo entre eles                                                                                #
########################################################################################################################
from time import sleep                                 # Importa o módulo 'sleep' da biblioteca 'time' para pausar a execução do programa.
for c in range(10, 0, -1):                             # Loop for que faz uma contagem regressiva de 10 até 1.
    print('          {}'.format(c))                    # Imprime os números da contagem com espaços para alinhar à direita.
    sleep(1)                                           # Pausa a execução do programa por 1 segundo.
print('\U0001F973'*5, '\U0001F4A5'*3, '\U0001F973'*5)  # Imprime uma linha de emojis representando comemoração e fogos de artifício.
print('        Feliz Ano novo!       ')                # Imprime a mensagem "Feliz Ano Novo!" no centro.
