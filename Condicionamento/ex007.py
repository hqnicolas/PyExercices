########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 34 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
########################################################################################################################
# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salários Superiores a R$1250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
########################################################################################################################
########################################################################################################################
########################################################################################################################
s = float(input('Digite o salario R$: '))
if s > 1250:
    t = (s + (s*10/100))                                        # Se o salário for maior que R$1250, calcula um aumento de 10%
    p = 10
else:
    t = (s + (s*15/100))                                        # Se o salário for igual ou menor a R$1250, calcula um aumento de 15%
    p = 15
print('O salario R${},\nRecebeu um aumentou de {}%\nagora o salário é: R${}'.format(s, p, t))
