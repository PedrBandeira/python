# Faça um programa que abra e reproduza o áudio de um arquivo mp3
import pygame

# Inicia o módulo de áudio
pygame.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('../audio/audio.mp3')

# Inicia a reprodução do arquivo
pygame.mixer.music.play()

# Mantém o programa em execução enquanto o áudio está sendo reproduzido
pygame.event.wait()