######################################################################################
#  Script Python escrito em 07/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '3b' do curso cursoemvideo.com                                   #
######################################################################################
s = input('Digite algo: ')                                     # a variável "s" Recebe um valor String do teclado
print('Qual classe?: ',type(s))                                # Print identifica o tipo de variável s
print('é numero?: ', s.isnumeric())                            # Print identifica se é numero a variável s
print('é letra?: ', s.isalpha())                               # Print identifica se é letra a variável s
print('O valor int é: ', s)                                    # Print exibe concatenada a variável s python2
print('O valor int é: {}' .format(s))                          # Print exibe dentro da string a variável s python3
i = int(input('Digite um int: '))                              # a variável "i" Recebe um valor int do teclado
print('Qual classe?: ',type(i))                                # Print identifica o tipo de variável i
print('O valor int é: ', i)                                    # Print exibe concatenada a variável i python2
print('O valor int é: {}' .format(i))                          # Print exibe dentro da string a variável i python3
f = float(input('Digite um Float: '))                          # a variável "f" Recebe um valor Float do teclado
print('Qual classe?: ',type(f))                                # Print identifica o tipo de variável f
print('é numero?: ', f.is_integer())                           # Print identifica se é numero a variável f                                               # Print identifica o tipo de variável f
print('O valor float é: ', f)                                  # Print exibe concatenada a variável f python2
print('O valor int é: {}' .format(f))                          # Print exibe dentro da string a variável f python3
b = bool(input('Digite um boolean: '))                         # a variável "b" Recebe um valor boolean do teclado
print('Qual classe?: ',type(b))                                # Print identifica o tipo de variável b                                           # Print identifica o tipo de variável b
print('O valor boolean é: ', b)                                # Print exibe concatenada a variável b python2
print('O valor salvo é: {}' .format(b))                        # Print exibe dentro da string a variável b python3
