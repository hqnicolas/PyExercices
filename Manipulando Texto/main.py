######################################################################################
######################################################################################
######################################################################################
#  Script Python escrito em 10/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com  Tratamento e manipulação de cadeias de texto   #
######################################################################################
######################################################################################
######################################################################################
#     Funcionalidades específicas para manipular string str ou cadeia de texto       #
######################################################################################
# String:                                                                            #
# frase = 'Curso em Video Python'                                                    #
######################################################################################
######################################################################################
######################################################################################
# len(frase)                                                                         #
# retorna o valor de comprimento da string "frase"                                   #
######################################################################################
# frase.count('o')                                                                   #
# conta o número de strings com a letra "o" minúscula                                #
# frase.count('o',0,13)                                                              #
# Contagem já com fatiamento                                                         #
######################################################################################
# frase.find('deo')                                                                  #
# retorna o numero do campo dentro da string onde começa o texto "deo"               #
######################################################################################
# 'curso' in frase                                                                   #
# retorna true pois tem sim uma palavra curso dentro da string frase                 #
######################################################################################
# frase.find('Android')                                                              #
# retorna o valor "-1" pois esta string não foi encontrada dentro da string frase    #
######################################################################################
######################################################################################
######################################################################################
# Fatiamento de String na memória:                                                   #
# C u r s o   e m   V i d e o   P y t h o n                                          #
# 0 1 2 3 4 5 6 7 8 9 1 1 2 3 4 5 6 7 8 9 2                                          #
######################################################################################
# Estrutura de dados "lista"                                                         #
# frase[9] == V                                                                      #
# no campo 9 da String temos o caractére ASCII                                       #
######################################################################################
# Estrutura de dados "lista"                                                         #
# frase[9:13] == Vide                                                                #
# no campo de 9 á 13 da String temos 4 caracteres                                    #
######################################################################################
# Estrutura de dados "lista"                                                         #
# frase[9:21:2] == VdoPto                                                            #
# no campo de 9 á 21 da String é pulado de 2 em 2                                    #
######################################################################################
# Estrutura de dados "lista"                                                         #
# frase[:5] == Curso                                                                 #
# do inicio absoluto até o caractere 5 é capturado                                   #
######################################################################################
# Estrutura de dados "lista"                                                         #
# frase[15:] == Python                                                               #
# do caractere 15 até o final absoluto é capturado                                   #
######################################################################################
# Estrutura de dados "lista"                                                         #
# frase[9::3] == VePh                                                                #
# do caractere 9 até o final absoluto é capturado pulando de 3 em 3                  #
######################################################################################
######################################################################################
######################################################################################
frase = 'Curso em Video Python'
frase.replace('Python','Android')
frase.upper()           # Torna os caracteres minúsculos maiúsculos
frase.lower()
frase.capitalize()      # Joga todos os caractéres para minusculo e joga a letra "0" para maiúscula
frase.title()           # Joga todos os caractéres para minusculo e joga as letras após espaço para maiúscula
frase.strip()           # Remove os espaços extras no inicio e no fim da frase
frase.rstrip()          # Remove espaços "right" do final da frase
frase.lstrip()          # Remove espaços "left" do inicio da frase
######################################################################################
######################################################################################
######################################################################################
frase.split()           # Por padrão é feito split pelos espaços e cria uma divisão  #
# C u r s o   e m   V i d e o   P y t h o n                                          #
# 0 1 2 3 4   0 1   0 1 2 3 4   0 1 2 3 4 5                                          #
#     0        1        2            3                                               #
# cada palavra recebe uma nova indexação e coloca em nova lista                      #
# Cada palavra recebe uma nova numeração                                             #
######################################################################################
######################################################################################
######################################################################################
# '-'.join(frase)                                                                    #
# Usando o separador "-" este comando reagrupa os caracteres em uma frase            #
######################################################################################
######################################################################################
######################################################################################
