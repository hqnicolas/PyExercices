########################################################################################################################
#  Script Python escrito em 19/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 047 laço de Repetição FOR             #
########################################################################################################################
# Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50                       #
########################################################################################################################
print('Todos os numeros pares entre 1 e 50')
for n in range(1, 51):                           # Verifica se o número é par (divisível por 2).
    if n % 2: print(end='{}, '.format(n+1))

print('')
print('Todos os numeros pares entre 1 e 50')
for n in range(2, 51, 2):
    print(end='{}, '.format(n))
