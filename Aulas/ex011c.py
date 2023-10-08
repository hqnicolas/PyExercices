######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '11' do curso cursoemvideo.com da aula 7 de operadores           #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==                                          #
######################################################################################
# um script que leia um numero inteiro qualquer e mosrte na tela a sua tabuada       #
######################################################################################
print('Calculadora de Tabuada')                                    # Apresentação do Script
def t(n):                                                          # Função para calcular a tabuada de um número
    print('Tabuada de {}:' .format(n))                             # Apresenta a função antes do loop
    for i in range(1, 11):                                         # define um loop em função de "i" de 1 á 10
        r = n * i                                                  # Calcula repetidas vezes o resultado da tabuada
        print("{} x {} = {}" .format(n, i, r))                     # Retorna repetidas vezes o resultado em tela
try:                                                               # inicio do tratamento de excessões
    n = int(input("Digite um número inteiro: "))                   # Solicita ao usuário que insira um número inteiro
    t(n)                                                           # Chama a função para calcular e exibir a tabuada
except ValueError:                                                 # caso haja exceções
    print("Por favor, insira um número inteiro válido.")           # informa ao usuário que prompt não foi aceito
