########################################################################################################################
#  Script Python escrito em 14/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com Desafio 39 condições e Repetições de codigo              #
########################################################################################################################
# Faça um programa que leia o ano de nascimento de um jovem informe, de acordo com sua idade.                          #
#  - Se ele ainda vai ser alistar ao serviço militar.                                                                  #
#  - Se é a hora de se alistar                                                                                         #
#  - Se já passou do tempo do alistamento.                                                                             #
# Seu script também deverá mostrar o tempo que falta ou que passou do prazo                                            #
########################################################################################################################
from datetime import date
n = int(input('Digite o ano em que você nasceu '))
d = str(date.today())
a = int(d[:4])
i = a - n
print('* Você tem {} anos. * '.format(i))
if 19 > i > 16:
    print('* Procure a Junta de serviço militar *')
elif i > 18:
    print('* Você está atrasado para o alistamento em {} anos *'.format(i - 18))
elif i < 17:
    print('* Faltam {} anos para o alistamento *'.format(18 - i))
