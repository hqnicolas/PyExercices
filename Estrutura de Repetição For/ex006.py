########################################################################################################################
#  Script Python escrito em 24/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 051 laço de Repetição FOR             #
########################################################################################################################
# Desenvolva um programa que leia o primeiro termo e a razão de uma Progreção aritimetica.                             #
# No final, mostre os 10 primeiros termos dessa progressão                                                             #
########################################################################################################################
print('10 Primeiros termos de uma PA')                                      # Imprime um cabeçalho informativo
p = int(input('Digite o primeiro termo: '))                                 # Solicita ao usuário que digite o primeiro termo da PA
c = int(input('Digite a razão da progressão: '))                            # Solicita ao usuário que digite a razão da PA
for i in range(p, (p+(10*c)), c):                                           # Inicia um loop que gera os 10 primeiros termos da PA
    print('{}'.format(i))                                                   # Imprime o termo atual

