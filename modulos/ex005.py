######################################################################################
#  Script Python escrito em 09/10/2023 por Nicolas Pereira no Jetbrains Pycharm      #
#  Exercício Numero '21' do curso cursoemvideo.com da aula 8  DESAFIO 021            #
######################################################################################
#  faça um programa em python que abra e reproduza um audio de arquivo mp3           #
######################################################################################
import pygame
pygame.init()
pygame.mixer.music.load('ex005.mp3')
pygame.mixer.music.play()
pygame.event.wait()

