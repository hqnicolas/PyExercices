########################################################################################################################
#  Script Python escrito em 14/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 38 condições e Repetições de codigo              #
########################################################################################################################
# Escreva um script que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:                       #
# - O primenro valor é maior                                                                                           #
# - O segundo valor é maior                                                                                            #
# - Não existe valor maior os dois são iguais                                                                          #
########################################################################################################################
print('* Comparador de variáveis *')
a1 = input('* Digite o primeiro valor: ')
a2 = input('* Digite o segundo valor: ')
b = [a1, a2]                                          # Cria uma lista 'b' contendo os valores 'a1' e 'a2'.
b.sort(reverse=True)                                  # Classifica a lista 'b' em ordem decrescente
c = b.index(a1)                                       # de modo que o maior valor fica na primeira posição.
if c == 0 and a1 != a2:                               # Verifica se o índice 'c' é 0 e se 'a1' é diferente de 'a2'.
    print('* O primeiro Valor é Maior *')
    print('* O Segundo Valor é Menor* ')
elif c == 1 and a1 != a2:                             # Verifica se o índice 'c' é 1 e se 'a1' é diferente de 'a2'.
    print('* O primeiro Valor é Menor *')
    print('* O segundo Valor é Maior *')
else:
    print('* Ambos os valores são iguais *')
########################################################################################################################

