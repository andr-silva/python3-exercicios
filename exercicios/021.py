# Faça um programa em Python que abra e reproduxza um áudio de um arquivo.mp3

import pygame

pygame.init()
pygame.mixer.music.load('assets/021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
