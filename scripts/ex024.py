# Faça um programa que abra e reproduza o áudio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('../audio/audio.mp3')
pygame.mixer.music.play()
