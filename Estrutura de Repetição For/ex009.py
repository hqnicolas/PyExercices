########################################################################################################################
#  Script Python escrito em 26/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 054 laço de Repetição FOR             #
########################################################################################################################
# Crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas ainda não atingiram   #
# a maioridade e quantas já são maiores de 21 anos                                                                     #
########################################################################################################################
from datetime import date                                               # Importa a classe 'date' do módulo 'datetime'
h = int(date.today().year)                                              # Obtém o ano atual e o armazena na variável 'h'
m = 0                                                                   # Inicializa as variáveis 'm' e 'k'
k = 0                                                                   # para contar as pessoas com 21 anos ou mais e com menos de 21 anos
for i in range(1, 8):                                                   # Loop para coletar o ano de nascimento de sete pessoas
    s = int(input('em qual ano a pessoa {} nasceu? '.format(i)))        # Solicita o ano de nascimento
    if (h - s) < 21:
        k += 1                                                          # Incrementa 'k' se a pessoa tiver menos de 21 anos
    elif (h - s) >= 21:
        m += 1                                                          # Incrementa 'm' se a pessoa tiver 21 anos ou mais
print('destes, {} São menores de 21'.format(k))                         # Exibe o número de pessoas menores de 21 e o número de pessoas com 21 anos ou mais
print('outros {} São maiores de 21'.format(m))
