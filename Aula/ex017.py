######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '17' do curso cursoemvideo.com da aula 7  DESAFIO 015            #
######################################################################################
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro       #
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar#
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.                     #
######################################################################################
km = float(input('Quantos quilometros rodados?: '))  # Solicita a quantidade de km
d = float(input('Quantos dias usado?: '))            # Solicita quantos dias foram usados
cd = d * 60                                          # calcula o custo do tempo de uso
ckm = km * 0.15                                      # calcula o custo da kilometragem
c = ckm + cd                                         # soma os dois valores
print('O Custo total foi de {}R$'.format(c))         # entrega o resultado
