########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 33 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
########################################################################################################################
# Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
########################################################################################################################
########################################################################################################################
########################################################################################################################
a = int(input('Digite o Primeiro numero: '))                               # Solicita ao usuário que insira 3 numeros
b = int(input('Digite o Segundo numero: '))
c = int(input('Digite o Terceiro numero: '))
d = [a, b, c]                                                              # Cria uma lista 'd' contendo os números 'a', 'b' e 'c'
d.sort(reverse=True)                                                       # Classifica a lista 'd' em ordem decrescente (do maior para o menor)
print('Maior: {}\n Médio: {}\n Menor: {}'.format(d[0], d[1], d[2]))        # Exibe os valores na lista 'd',
                                                                    # onde o primeiro elemento é o maior, o segundo é o do meio e o terceiro é o menor
