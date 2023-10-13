########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 29 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
# Escreva um Script que leia a velocidade de um carro
# se ele ultrapasar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# a multa vai custar R$7,00 por cada km acima do limite
########################################################################################################################
########################################################################################################################
########################################################################################################################
v = float(input('Digite a velocidade do carro km/h: '))        # Solicita ao usuário que insira a velocidade do carro em km/h
if v > 80:                                                     # e armazena o valor como um número de ponto flutuante na variável 'v'
    print('Você foi multado! em R${}.'.format((v - 80) * 7))   # Se a velocidade for superior a 80 km/h, calcula a multa com base na diferença
                                                               # entre a velocidade e 80 km/h multiplicada por R$7 (valor da multa por km/h acima do limite)
                                                               # Exibe a mensagem informando ao motorista que ele foi multado e mostra o valor da multa
