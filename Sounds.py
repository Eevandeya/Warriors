import pygame

pygame.mixer.init()

hit_sound = pygame.mixer.Sound('sounds/hit.wav')
shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
win_sound = pygame.mixer.Sound('sounds/win.wav')

hit_sound.set_volume(0.1)
shoot_sound.set_volume(0.1)
explosion_sound.set_volume(0.3)
win_sound.set_volume(0.3)
