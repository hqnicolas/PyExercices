########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 28 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
# Escreva um programa que faça o computador "pensar" em um numero inteiro entre "0" e "5"
# e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
# o script deverá escrever na tela se o usuario venceu ou perdeu
########################################################################################################################
########################################################################################################################
########################################################################################################################
from random import randint                                      # Importa a função do módulo para gerar números aleatórios
from time import sleep
n = randint(0, 5)                                               # Gera um número aleatório entre 0 e 5 e o armazena na variável 'n'
print('Eu pensei em um número')                                 # Exibe uma mensagem para informar ao jogador que um número foi escolhido
i = int(input('Vamos lá, Adivinhe um número de 0 á 5: '))       # Solicita que o jogador insira um palpite de número entre 0 e 5 e armazena na variável 'i'
sleep(3)
if i == n:                                                      # Verifica se o palpite do jogador ('i') é igual ao número aleatório ('n')
    print('-=-' * 20)                                           # Se o palpite estiver correto, exibe uma mensagem de acerto
    print('Você acertou!')
    print('-=-' * 20)
else:                                                           # Se o palpite estiver errado, exibe uma mensagem de erro
    print('Você errou!')
print('Vamos denovo.')                                          # Encerra o jogo ou indica que é hora de jogar novamente
