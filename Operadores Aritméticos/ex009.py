######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '9' do curso cursoemvideo.com da aula 7 de operadores            #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==        DESAFIO 007                       #
######################################################################################
# desenvolva um programa que leia as duas notas de um aluno, calcule e moste a media #
######################################################################################
print('Calculadora de média')                                    # Apresentação do Script
n1 = float(input('digite a nota da Primeira Avaliação: '))       # Solicita a nota para a variável float "n1"
n2 = float(input('digite a nota da Segunda Avaliação: '))        # Solicita a nota para a variável float "n2"
r = ((n1 + n2) / 2)                                              # Efetua o calculo da média
print('A média deste aluno foi: {:.1f}' .format(r))              # Retorna o resultado
