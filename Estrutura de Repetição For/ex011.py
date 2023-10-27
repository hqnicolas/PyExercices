########################################################################################################################
#  Script Python escrito em 26/10/2023 por Nicolas Pereira no Jetbrains Pycharm                                        #
#  aula 13 - nível médio do curso de python cursoemvideo.com exercicio de numero 056 laço de Repetição FOR             #
########################################################################################################################
# Crie um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre:                            #
# a media de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos                        #
########################################################################################################################
mn = 0                                                              # Variável para contar o número de mulheres com menos de 20 anos
hv = 0                                                              # Variável para rastrear a idade do homem mais velho
nn = []                                                             # Lista para armazenar nomes
aa = []                                                             # Lista para armazenar idades
ss = []                                                             # Lista para armazenar sexos
i: int                                                              # Variável de iteração (não é necessário declarar i como int)
for i in range(1, 5):                                               # Loop para coletar informações de 4 pessoas
    print('#'*10, '{}ª Pessoa'.format(i), '#'*10)
    n = str(input('Nome: '))
    nn.append(n)
    a = int(input('idade: '))
    aa.append(a)
    s = str.lower(input('sexo[M/F]: '))
    ss.append(s)
    if s == ('f') and a < 20:                                       # Verifica se a pessoa é do sexo feminino e tem menos de 20 anos
        mn += 1
    if hv == 0 and s == ('m'):                                      # Verifica a idade do homem mais velho
        hv = a
        hvi = i
    elif i != 1 and s == ('m') and a > hv:
        hv = a
        hvi = i
soma = sum(aa)                                                      # Calcula a média das idades
media = soma / 4
print('A média de indade é de {} anos.'.format(media))              # Exibe os resultados
print('O homem mais velho é {}, ele tem {} anos.'.format(nn[hvi -1], aa[hvi -1]))
print('{} mulher(es) tem menos de 20 anos.'.format(mn))


