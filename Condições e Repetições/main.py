########################################################################################################################
#  Script Python escrito em 13/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com  condições e Repetições de codigo                        #
########################################################################################################################
# Condições aninhadas são:
# Estruturas condicionadas, uma dentro da outra.
#
# a estrutura condicional if tem somente 2 opções
# para aumentar o número de opções pode ser usada a estrutura de condição aninhada
#
#######################################################################################################################

carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão se carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
senão
    carro.siga()
carro.pare()

##########################################################

if carro.esquerda():

    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()

elif carro.ré():
     carro.siga()

elif carro.direita():

    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()

else
    carro.siga()

carro.pare()

##########################################################
