########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 32 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
########################################################################################################################
# faça um programa que leia um ano qualquer e mostre se ele é bissexto
########################################################################################################################
########################################################################################################################
########################################################################################################################
a = int(input('Digite um ano:'))                             # Solicita ao usuário que insira um ano e armazena o valor como um número inteiro na variável 'a'
if ((a % 100 != 0) and (a % 4 == 0)) or (a % 400 == 0):      # Verifica se o ano é bissexto usando uma combinação de operadores lógicos
    print('Esse ano é')                                      # Se a condição for verdadeira, exibe 'Esse ano é'
else:                                                        # Se a condição for falsa, exibe 'é nada'
    print('é nada')
########################################################################################################################
b = not(bool(a % 4))                                         # Calcula valores booleanos com base nas regras de anos bissextos
c = bool(a % 100)
d = not(bool(a % 400))
if (b and c) or d:                                           # Verifica se o ano é bissexto usando variáveis booleanas 'b', 'c' e 'd'
    print('Bissexto!')                                       # Se a condição for verdadeira, exibe 'Bissexto!'
else:                                                        # Se a condição for falsa, exibe 'Esse ano é Comum.'
    print('Esse ano é Comum.')
########################################################################################################################
