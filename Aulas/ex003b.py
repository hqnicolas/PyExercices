######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '3' do curso cursoemvideo.com                                    #
######################################################################################

print(' Calculadora de Soma ')                                # Imprime um cabeçalho para a calculadora
n1 = int(input('Digite um Número: '))                         # Solicita ao usuário para inserir o primeiro número
n2 = int(input('Digite outro Número: '))                      # Solicita ao usuário para inserir o segundo número
s = n1 + n2                                                   # Calcula a soma dos dois números inseridos
print('A soma Vale: ', s)                                     # Imprime a soma usando uma string com espaços
print('A soma entre {} + {} Vale:{}' .format(n1, n2, s))      # Imprime a soma usando uma string formatada
