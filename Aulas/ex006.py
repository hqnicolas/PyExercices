######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '6' do curso cursoemvideo.com                                    #
#  Faça um programa que solicite 2 valores e retorne a soma deles                    #
######################################################################################
# Imprime um título para a calculadora
print('Calculadora de Soma')

# Solicita ao usuário para digitar o primeiro número e armazena-o em 'n1' como um número inteiro
n1 = int(input('Digite um Número: '))

# Solicita ao usuário para digitar o segundo número e armazena-o em 'n2' como um número inteiro
n2 = int(input('Digite outro Número: '))

# Realiza a soma dos números digitados e armazena o resultado em 's'
s = n1 + n2

# Imprime a soma dos números formatada na tela
print('A soma entre {} e {} é: {}'.format(n1, n2, s))
