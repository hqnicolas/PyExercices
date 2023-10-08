######################################################################################
#  Script Python escrito em 08/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '14' do curso cursoemvideo.com da aula 7  DESAFIO 014            #
######################################################################################
# converta uma temperatura digitando Celsius e converta para graus Fahrenheit.       #
######################################################################################
c = float(input('informe a temperatura em ºc: ')) # Solicita ao usuário que insira a temperatura em graus Celsius (°C) e armazena o valor em 'c'.
g = c * 1.8                                       # Converte a temperatura de graus Celsius (°C) para graus Fahrenheit (°F) usando a fórmula correta.
f = g + 32                                        # Imprime uma mensagem com a temperatura em graus Celsius (°C) e a correspondente temperatura em graus Fahrenheit (°F).
print('A temperatura de {:.1f}ºC corresponde á {:.1f}ºF' .format(c, f))
