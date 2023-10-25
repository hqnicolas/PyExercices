########################################################################################################################
#  Script Python escrito em 24/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 052 laço de Repetição FOR             #
########################################################################################################################
# Desenvolva um programa que leia um numero intenro e diga se ele é ou não um numero primo "divisivel por 1 e por ele" #
########################################################################################################################
print('Número Primo?')                                           # Imprime um cabeçalho informativo
d = 0                                                            # Inicializa uma variável 'd' para armazenar a soma dos divisores
n = int(input('Digite um número: '))                             # Solicita ao usuário que digite um número e o armazena em 'n'
for i in range(1, n + 1):                                        # Inicia um loop que verifica divisores do número 'n'
    if n % i == 0:
        print('divisível por: {}'.format(i))                     # Imprime os divisores encontrados
        d += i
if d == (n + 1):                                                 # Verifica se a soma dos divisores é igual a 'n + 1' (condição para ser primo)
        print('O número {} é primo!'.format(n))                  # Se a condição for verdadeira, o número é primo
else:
        print('O número {} não é primo!'.format(n))              # Se a condição for falsa, o número não é primo
