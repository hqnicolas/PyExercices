########################################################################################################################
#  Script Python escrito em 25/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 053 laço de Repetição FOR             #
########################################################################################################################
# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços               #
# APOS A SOPA               é a mesma frase de trás para frente                  a torre da derrota                    #
########################################################################################################################
print('* Detector de Texto Palindromo *')
i = str(input('Digite o texto: '))                  # Obtenha a entrada do usuário
s = i.replace(' ','').lower()                       # remove todos os espaços e coloca tudo em caixa baixa
i = s[::-1]                                         # transfere o texto invertido para a variavel i
if i == s:                                          # Verifique se a frase é um palíndromo
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada é normal.')
