######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '14' do curso cursoemvideo.com da aula 7  DESAFIO 012            #
######################################################################################
#   leia o preço de um produto e mostre seu novo preço, com 5% de desconto.          #
######################################################################################
p = float(input('Qual é o preço do produto? R$'))                                    # Solicita ao usuário que insira o valor do produto
d = p * (5/100)                                                                      # calcula o valor do desconto em reais
n = p - d                                                                            # calcula o novo valor do produto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}' .format(p, n))
