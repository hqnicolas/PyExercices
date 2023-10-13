########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 30 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar#
########################################################################################################################
########################################################################################################################
########################################################################################################################
n = int(input('Digite um número: '))            # Solicita ao usuário que insira um número e armazena o valor como um número inteiro na variável 'n'
p = bool(n % 2)                                 # Calcula o resto da divisão de 'n' por 2 e converte o resultado em um valor booleano
if p:                                           # Se o resto for 0, 'p' será False (indicando que o número é par); caso contrário, 'p' será True (indicando que o número é ímpar)
    print('O numero {} é impar'.format(n))      # Verifica se 'p' é True (indicando que o número é ímpar) e exibe uma mensagem correspondente
else:                                           # Se 'p' for False, exibe uma mensagem indicando que o número é par
    print('O numero {} é par'.format(n))
