########################################################################################################################
#  Script Python escrito em 15/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 41 condições e Repetições de codigo              #
########################################################################################################################
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre         #
# sua categoria, de acordo com a idade:                                                                                #
# até 9 anos: MIRIM                                                                                                    #
# até 14 anos: INFANTIL                                                                                                #
# até 19 anos: JUNIOR                                                                                                  #
# até 20 anos: SÊNIOR                                                                                                  #
# acima 20 anos: MASTER                                                                                                #
########################################################################################################################
print('* Classificador de Nadadores *')                     # Título informativo
n = int(input('Digite o ano de nascimento: '))              # Solicita ao usuário o ano de nascimento e armazena na variável 'n'
from datetime import date                                   # Importa o módulo 'date' da biblioteca 'datetime' e obtém o ano atual em 'd'
d = date.today().year
i = d - n                                                   # Calcula a idade do nadador subtraindo o ano de nascimento do ano atual
if i <= 9:                                                  # Com base na idade, determina a categoria do nadador e exibe a categoria correspondente
    print('Categoria: MIRIM!')
elif 9 < i <= 14:
    print('Categoria: INFANTIL!')
elif 14 < i <= 19:
    print('Categoria: JUNIOR!')
elif 19 < i <= 20:
    print('Categoria: SÊNIOR!')
elif i > 20:
    print('Categoria: MASTER!')
