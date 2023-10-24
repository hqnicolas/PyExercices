########################################################################################################################
#  Script Python escrito em 19/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de estrutura de laço de Repetição FOR           #
########################################################################################################################
for i in range(0, 6):
    print('oi')
print('fim')
########################################################################################################################
for i in range(6, 0, -1):
    print(i)
print('fim')
########################################################################################################################
for i in range(0, 7, 2):
    print(i)
    print('{}'.format(i))
print('fim')
########################################################################################################################
n = int(input('Digite um número: '))
for i in range(0, n+1):
    print(i)
print('fim')
########################################################################################################################
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for n in range(i, f+1, p):
    print(n)
print('fim')
########################################################################################################################
s = 0                                                               # inicia a variável
for c in range(0, 4):                                               # inicia o loop for
    n = int(input('Digite um valor:'))                              # pede 4 numeros
    s += n                                      # somatório s = s + n
print('O somatório de todos os valores foi {}'.format(s))
print('fim')
########################################################################################################################
