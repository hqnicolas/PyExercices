########################################################################################################################
#  Script Python escrito em 13/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 36 condições e Repetições de codigo              #
########################################################################################################################
# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.                                    #
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.                    #
# Calcule o valor da prestação mensar sabendo que ele não pode exceder 30% do salário                                  #
# ou então o empréstimo será negado                                                                                    #
########################################################################################################################
print('* Programa para aprovação de crédito *')
v = float(input('* Qual o valor do imóvel? R$ '))
s = float(input('* Qual o salário do comprador? R$ '))
t = float(input('* Em quantos anos será financiado? '))
m = t * 12
p = v / m
print('* Para pegar uma casa de R${:.1f}\n* Com prazo de {:.1f} anos\n* Foi Aprovado!'.format(v, t, p))
if p > (s * 30 / 100):
    print('*\n* Seu empréstimo foi negado.\n*\n')
else:
    print('* Seu empréstimo tem duração de {:.0f} meses, \n* com parcelas de R${:.2f} mensais.'.format(m, p))
