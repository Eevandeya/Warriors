import pygame

pygame.mixer.init()

kiki_shot = pygame.mixer.Sound('sounds/кирилл-стреляет.wav')
kiki_death = pygame.mixer.Sound('sounds/кирилла-убили.wav')
kiki_hit = pygame.mixer.Sound('sounds/в-кирилла-попали.wav')

dada_shot = pygame.mixer.Sound('sounds/даня-стреляет.wav')
dada_death = pygame.mixer.Sound('sounds/даню-убили.wav')
dada_hit = pygame.mixer.Sound('sounds/в-даню-попали.wav')

win_sound = pygame.mixer.Sound('sounds/win.wav')
switch_sound = pygame.mixer.Sound('sounds/switch.wav')
pick_sound = pygame.mixer.Sound('sounds/pick.wav')

pick_sound.set_volume(0.5)
switch_sound.set_volume(0.5)
kiki_hit.set_volume(0.5)
kiki_death.set_volume(0.6)
kiki_shot.set_volume(0.1)

win_sound.set_volume(0.5)

dada_hit.set_volume(0.5)
dada_death.set_volume(0.6)
dada_shot.set_volume(0.15)
