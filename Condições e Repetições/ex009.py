########################################################################################################################
#  Script Python escrito em 15/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 44 condições e Repetições de codigo              #
########################################################################################################################
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição        #
# de pagamento:                                                                                                        #
# á Vista Dinheiro/cheque: 10% de desconto                                                                             #
# á Vista no cartão: 5% de desconto                                                                                    #
# em até 2x no cartão: preço normal                                                                                    #
# 3x ou mais no cartão: 20% de juros                                                                                   #
########################################################################################################################
from time import sleep
print('* Guichê de pagamentos *')
v = float(input('Digite o valor á ser pago: R$'))
print('* Condições de Pagamento *\n- Em Dinheiro: 1\n- Débito: 2\n- Até 2x no Crédito: 3\n- Acima de 3x no crédito: 4')
o = int(input('Selecione de 1 á 4 sua opção: '))
if o == 1:
    t = v - (v * 10 / 100)
    print('* Você Selecionou Pagamento em dinheiro! *\n- O Valor Total é de: R${:.2f}'.format(t))
elif o == 2:
    t = v - (v * 5 / 100)
    print('* Você Selecionou Pagamento com Cartão de débito! *\n- O Valor Total é de: R${:.2f}'.format(t))
elif o == 3:
    print('* Você Selecionou Pagamento em até 2x no crédito! *\n- O Valor Total é de: R${:.2f}'.format(v))
elif o == 4:
    t = v + (v * 20 / 100)
    print('* Você Selecionou Pagamento em mais de 3x no crédito! *\n- O Valor Total é de: R${:.2f}'.format(t))
else:
    print('* Opção invalida *')
input('Enter para confirmar.')
