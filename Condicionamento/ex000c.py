########################################################################################################################
#  Script Python escrito em 11/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  10ª aula do curso cursoemvideo.com exemplo 1 do condicionamento de codigo em python                                 #
########################################################################################################################
nome = str(input('Qual é seu nome? '))                            # Solicita o nome do usuário e armazena na variável 'nome'
if nome == 'Nicolas':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')                               # Saudação genérica 'Bom dia!' seguida pelo nome do usuário
print('Bom dia! {}'.format(nome))
########################################################################################################################
n1 = float(input('Digite a primeira nota:'))                      # Solicita a inserção de duas notas e as armazena nas variáveis 'n1' e 'n2'
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2                                                   # Calcula a média das duas notas e armazena em 'm'
print('A sua média foi {:.1f}'.format(m))                         # Imprime a média formatada com uma casa decimal
if m>= 6.0:                                                       # Verifica se a média é maior ou igual a 6.0 e imprime mensagens de acordo com a condição
    print('Sua Média foi boa! ')
else:
    print('Sua média foi ruim, {} ESTUDE MAIS!'.format(nome))
########################################################################################################################
print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!')                    # 'PARABÉNS' se a média for maior ou igual a 6, caso contrário, imprime 'ESTUDE MAIS!'
########################################################################################################################
########################################################################################################################
