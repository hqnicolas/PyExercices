########################################################################################################################
#  Script Python escrito em 12/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com desafio 35 do condicionamento de codigo em python                                #
########################################################################################################################
########################################################################################################################
# Desenvolva um programa que leia o comprimeito de três retas e diga ao usuario se elas podem ou não formar um triangulo
########################################################################################################################
########################################################################################################################
########################################################################################################################
print('Digite os três lado do Triangulo')                            # Solicita ao usuário que insira os três lados do triângulo
a = float(input('lado a: '))
b = float(input('lado b: '))
c = float(input('lado c: '))
if a + b < c or c + b < a or a + c < b:                              # Verifica se é possível formar um triângulo com os lados fornecidos
    print('!Este triangulo não é possível!')
else:
    print('Podemos chamar de triangulo {:.1f} - {:.1f} - {:.1f}'.format(a, b, c))
