########################################################################################################################
#  Script Python escrito em 15/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 45 condições e Repetições de codigo              #
########################################################################################################################
# Crie um programa que faça o computador jogar Joquenpô com você: Pedra, Papel ou tezoura                              #
########################################################################################################################
from random import randint
print('* Vamos Jogar Joquenpô *')
print('Pedra: 1\nPapel: 2\nTesoura: 3')
p = randint(1, 3)                               # Gere uma escolha aleatória para o computador (Pedra, Papel ou Tesoura).
u = int(input('\n1, 2 ou 3? '))
if p == u:                                      # Verifique se a escolha do jogador é igual à escolha do computador.
    print('\nVocê Acertou!')
else:                                           # Se as escolhas forem diferentes, informe a escolha do computador.
    print('\nvocê errou! era {}'.format(p))
