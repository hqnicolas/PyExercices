######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '10' do curso cursoemvideo.com da aula 7 de operadores           #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==                  DESAFIO 008             #
######################################################################################
# leia um valor em metros e o exiba comvertido em centimetros e milimetros           #
######################################################################################
# | Km | hm | dam | m | dm | cm | mm|                                                #
#   0    0    0     0   0    0    0                                                  #
######################################################################################
print('Metros para centimetros! ')                   # Print em tela da descrição do script
print('use . ao invez de , ')
mt = float(input('Digite o Valor em Metros: '))      # Recebe o Valor em metros com virgola
nc = mt * 100                                        # calcula em centimetros
nci = int(nc)                                        # converte para um numero inteiro em centimetros
nm = mt * 1000                                       # calcula em milimetros
nmi = int(nm)                                        # converte para um numero inteiro em milimetros
print('O Valor em Centimetros é: {}cm'.format(nci))    # exibe o valor em centimetros
print('O Valor em milimetros é: {}mm'.format(nmi))     # exibe o valor em milimetros
