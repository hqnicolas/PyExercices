######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '5' do curso cursoemvideo.com    DESAFIO 003                     #
#  crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo #
######################################################################################
print('Programa que mostra informações sobre o input')         # Print em tela da descrição do script
a = input('Digite algo aqui: ')                                # Input recebe os valores string para variável "a"
print('"{}" é texto? '.format(a), a.isalpha())                 # Print informa se "a" contém texto
print('"{}" é número? '.format(a), a.isnumeric())              # Print informa se "a" contém número
print('"{}" tem qual tipo Primitivo? '.format(a), type(a))     # Print informa a Classe "tipo primitivo" de "a"
