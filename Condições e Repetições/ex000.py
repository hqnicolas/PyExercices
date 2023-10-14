########################################################################################################################
#  Script Python escrito em 13/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  1ª aula de nível médio do curso de python cursoemvideo.com  condições e Repetições de codigo                        #
########################################################################################################################
# Exemplo de estrutura Aninhada:
########################################################################################################################
nome - str(input('qual é seu nome? '))
if nome == ('Nicolas'):
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome é Popular no Brasil...')
elif nome in 'Ana Claudio Jessica Juliana':
    print('seu nome é feminino...')
else:
    print('seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))
########################################################################################################################
