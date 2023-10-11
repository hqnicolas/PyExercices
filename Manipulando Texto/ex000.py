######################################################################################
#  Script Python escrito em 10/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com exemplo 1 da manipulação de cadeias de texto    #
######################################################################################
frase = 'Curso em Video Python'                                                      #
print(frase[::2])                                                                    #
print(frase[1:15:])                                                                  #
print(frase[::2])                                                                    #
######################################################################################
print('Oi')                                                                          #
print(frase)                                                                         #
######################################################################################
# Frase á pesar de ser uma cadeia de caracteres, pode ser tratado como objeto
# portando você pode usar o comando frase.coisas
print(frase.count('o'))
# Este comando vai retornar "zero" devido a não haver "o" minusculo
print(frase.upper().count('o'))
# agora, com esta manipulação "upper" o comando count passa a encontrar "1"
# pois a manipulação de objeto levou a interação encontrar "O" maiúsculo
######################################################################################
print(len(frase.strip()))
print(len(frase))
print(frase)
print(frase.replace('Python','Android'))         # exibe a frase alterada com replace mas não salva na variável
print(len(frase))                                # notamos que o length continua o mesmo
print(frase)                                     # exibe a frase sem manipulação
frase = frase.replace('Python','Android')        # Atribui dentro da variavel frase a frase manipulada com replace
print(frase)                                     # exibe a frase manipulada com replace
######################################################################################
print("""Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer 
took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic 
typesetting, remaining essentially unchanged. It was popularised in the 1960s 
with the release of Letraset sheets containing Lorem Ipsum passages, and more 
recently with desktop publishing software like Aldus PageMaker including 
versions of Lorem Ipsum.""")



