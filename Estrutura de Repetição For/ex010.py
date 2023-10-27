########################################################################################################################
#  Script Python escrito em 26/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 055 laço de Repetição FOR             #
########################################################################################################################
# Faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e o menor peso lidos             #
########################################################################################################################
print('* Comparador de pesos *')                                    # Imprime uma mensagem de título
d = []                                                              # Inicializa uma lista vazia para armazenar os pesos
for i in range(1, 6):                                               # Loop para coletar o peso de 5 pessoas
    s = float(input('Digite o peso do {}º gordo:'.format(i)))       # Solicita o peso de uma pessoa
    d.append(s)                                                     # Adiciona o peso à lista 'd'
d.sort(reverse=True)                                                # Classifica a lista 'd' em ordem decrescente (do maior para o menor peso)
print('O Maior peso foi: {}kg'.format(d[0]))                        # Imprime o maior peso (primeiro item da lista 'd')
print('O mais leve é: {}kg'.format(d[4]))                           # Imprime o peso mais leve (último item da lista 'd' após a classificação)
