######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '15' do curso cursoemvideo.com da aula 7  DESAFIO 013            #
######################################################################################
# leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.    #
######################################################################################
s = float(input('Qual é o salário do Funcionário? R$')) # Solicita ao usuário que insira o salário do funcionário e armazena o valor em 's'.
a = s * (15/100)                                        # Calcula o aumento de 15% no salário 's' e armazena o resultado em 'a'.
r = a + s                                               # Calcula o novo salário 'r' somando o aumento 'a' ao salário original 's'.
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, r))
# Imprime uma mensagem com o salário original 's' e o novo salário 'r'.
