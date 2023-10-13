########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 31 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
########################################################################################################################
# Desenvolva um programa que pergunte a distância de uma viagem em KM
# Calcule o preço da passagem.
# cobrando R$0.50 por KM para viagens de até 200km
# e R$0.45 para viagens mais longas
########################################################################################################################
########################################################################################################################
########################################################################################################################
km = float(input('Digite a distância da viagem em KM: '))       # Solicita ao usuário que insira a distância da viagem em
if km <= 200: r = km * 0.5                                      # quilômetros e armazena o valor como um número de ponto flutuante na variável 'km'
else: r = km * 0.45                                             # Se a distância for menor ou igual a 200 km, o valor da cobrança é calculado multiplicando a distância por 0.5 (R$0.50 por quilômetro)
print('O valor para cobrança é: {}'.format(r))                  # Exibe o valor de cobrança da viagem
########################################################################################################################

