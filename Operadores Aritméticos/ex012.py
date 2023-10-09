######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '12' do curso cursoemvideo.com da aula 7 de operadores           #
#  Operadores Aritiméticos: ||| + ||| - | * ||| / ||| ** ||| // ||| % ||| == |||     #
#  Simbolo de igualdade para resultados  ==     DESAFIO 010                          #
######################################################################################
# um script que receba a informação do valor em reais e converta para dolares        #
######################################################################################
r = float(input('Quanto dinheiro você tem na carteira?  R$'))                   # solicita o valor para "r" em reais
x = float(input('qual á cotação do dolar hoje? R$'))                            # solicita a cotação do dolar "x" em reais
u = r/x                                                                         # Calcula
print('Com R${:.2f} você pode comprar US${:.2f}' .format(r, u))                 # Retorna o valor em Dólares com float de duas casas decimais
