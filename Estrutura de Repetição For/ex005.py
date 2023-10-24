########################################################################################################################
#  Script Python escrito em 19/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 050 laço de Repetição FOR             #
########################################################################################################################
# Desenvolva um programa que leia 6 numeros intenros e mostre a soma apenas daqueles que forem par                     #
########################################################################################################################
s = 0                                                       # Inicializa uma variável 's' para armazenar a soma dos números pares
for i in range(1, 7):                                       # Inicia um loop de 1 a 6 (inclusive), pois queremos coletar 6 números
    n = int(input('Digite o {}º Numero: '.format(i)))       # Solicita ao usuário que digite um número
    if n % 2 == 0:                                          # Verifica se o número digitado é par
        s += n                                              # Se o número for par, adiciona-o à soma 's'
print('A soma dos números pares é: {}'.format(s))           # Imprime a soma dos números pares
