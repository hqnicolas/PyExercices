######################################################################################
#  Script Python escrito em 11/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  9ª aula do curso cursoemvideo.com desafio 26 da manipulação de cadeias de texto   #
######################################################################################
# Faça um programa que leia uma frase pelo teclado e mostre:                         #
# Quantas vezes aparece a letra "A".                                                 #
# Em que posição ela aparece a primeira vez.                                         #
# Em que posição ela aparece a ultima vez.                                           #
######################################################################################
i = input('Digite um frase: ')           # Solicita ao usuário que digite uma frase e armazena a entrada em 'i'
f = i.lower()                            # Converte a frase para letras minúsculas (para não diferenciar maiúsculas de minúsculas)
a1 = f.count('a')                        # Conta quantas vezes a letra 'a' aparece na frase em minúsculas
p1 = f.find('a') +1                      # Encontra a posição (índice) da primeira ocorrência da letra 'a' e ajusta para começar de 1
p2 = f.rfind('a') +1                     # Encontra a posição (índice) da última ocorrência da letra 'a' e ajusta para começar de 1
print('A frase: {}. Possuí {} Letras "A", a primeira fica {} a ultima {} '.format(f, a1, p1, p2 ))
# Imprime a frase original em minúsculas, o número de letras 'a', a posição da primeira e da última 'a'
