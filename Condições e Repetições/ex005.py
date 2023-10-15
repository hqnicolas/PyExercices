########################################################################################################################
#  Script Python escrito em 15/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 40 condições e Repetições de codigo              #
########################################################################################################################
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final                #
# de acordo com a média atingida:                                                                                      #
# - Média abaixo de 5.0: Reprovado                                                                                     #
# - Média entre de 5.0 á 6.9: Recuperação                                                                              #
# - Média acima de 7.0: Aprovado                                                                                       #
########################################################################################################################
n1 = float(input('* Aluno, digite sua primeira nota: '))                  # Solicita ao aluno que digite sua primeira nota e armazena o valor como um número de ponto flutuante (float).
n2 = float(input('* Aluno, digite sua segunda nota: '))                   # Solicita ao aluno que digite sua segunda nota e armazena o valor como um número de ponto flutuante (float).
m = (n1 + n2) / 2                                                         # Calcula a média das duas notas.
if m < 5:                                                                 # Verifica a média (m) e determina o status do aluno com base na nota.
    print('* Você está Reprovado! Média: {:.2f} *'.format(m))             # Se a média for menor que 5, o aluno é considerado "Reprovado".
elif 7 > m > 4.9:                                                         # Se a média for maior ou igual a 5, mas menor que 7, o aluno está em "Recuperação".
    print('* Você está em Recuperação! Média: {:.2f} *'.format(m))
elif 7 <= m:                                                              # Se a média for 7 ou maior, o aluno está "Aprovado".
    print('* Você está Aprovado! Média: {:.2f} *'.format(m))
