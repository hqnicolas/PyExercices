########################################################################################################################
#  Script Python escrito em 15/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 43 condições e Repetições de codigo              #
########################################################################################################################
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo:       #
# - abaixo de 18.5: Abaixo do peso                                                                                     #
# - entre 18.5 e 25: Peso ideal                                                                                        #
# - 25 até 30: Sobre peso                                                                                              #
# - 30 até 40: Obesidade                                                                                               #
# - Acima de 40: Obesidade Mórbida                                                                                     #
########################################################################################################################
from math import pow                                         # Importa a função 'pow' do módulo 'math'
print('* Calculo de IMC *')
p = float(input('Digite seu peso: '))                        # Obtém a entrada do usuário para peso (p) e altura (a)
a = float(input('Digite sua altura: '))
imc = p / pow(a, 2)                                          # Calcula o IMC usando os valores inseridos
if imc < 18.5:                                               # Verifica o valor do IMC e exibe uma mensagem apropriada
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso peso!')
elif 30 <= imc < 40:
    print('Obesidade!')
elif 40 <= imc:
    print('Thais Carla?')
