import pygame

pygame.mixer.init()

dada_sounds = {'shot': pygame.mixer.Sound('sounds/family/dada_shot.wav'),
               'hit': pygame.mixer.Sound('sounds/family/dada_hit.wav'),
               'death': pygame.mixer.Sound('sounds/family/dada_death.wav'),
               'phrases': [pygame.mixer.Sound('sounds/family/dada_phrase_1.wav'),
                           pygame.mixer.Sound('sounds/family/dada_phrase_2.wav'),
                           pygame.mixer.Sound('sounds/family/dada_phrase_3.wav')]}


kiki_sounds = {'shot': pygame.mixer.Sound('sounds/family/kiki_shot.wav'),
               'hit': pygame.mixer.Sound('sounds/family/kiki_hit.wav'),
               'death': pygame.mixer.Sound('sounds/family/kiki_death.wav'),
               'phrases': [pygame.mixer.Sound('sounds/family/kiki_phrase_1.wav'),
                           pygame.mixer.Sound('sounds/family/kiki_phrase_2.wav'),
                           pygame.mixer.Sound('sounds/family/kiki_phrase_3.wav')]}


vava_sounds = {'shot': pygame.mixer.Sound('sounds/family/vava_shot.wav'),
               'hit': pygame.mixer.Sound('sounds/family/vava_hit.wav'),
               'death': pygame.mixer.Sound('sounds/family/vava_death.wav'),
               'phrases': [pygame.mixer.Sound('sounds/family/vava_phrase_1.wav'),
                           pygame.mixer.Sound('sounds/family/vava_phrase_2.wav'),
                           pygame.mixer.Sound('sounds/family/vava_phrase_3.wav')]}


papa_sounds = {'shot': pygame.mixer.Sound('sounds/family/papa_shot.wav'),
               'hit': pygame.mixer.Sound('sounds/family/papa_hit.wav'),
               'death': pygame.mixer.Sound('sounds/family/papa_death.wav'),
               'phrases': [pygame.mixer.Sound('sounds/family/papa_phrase_1.wav'),
                           pygame.mixer.Sound('sounds/family/papa_phrase_2.wav'),
                           pygame.mixer.Sound('sounds/family/papa_phrase_3.wav')]}


mama_sounds = {'shot': pygame.mixer.Sound('sounds/family/mama_shot.wav'),
               'hit': pygame.mixer.Sound('sounds/family/mama_hit.wav'),
               'death': pygame.mixer.Sound('sounds/family/mama_death.wav'),
               'phrases': [pygame.mixer.Sound('sounds/family/mama_phrase_1.wav'),
                           pygame.mixer.Sound('sounds/family/mama_phrase_2.wav'),
                           pygame.mixer.Sound('sounds/family/mama_phrase_3.wav')]}


character_sounds = [dada_sounds, kiki_sounds, vava_sounds, papa_sounds, mama_sounds]

win_sound = pygame.mixer.Sound('sounds/win.wav')
switch_sound = pygame.mixer.Sound('sounds/switch.wav')
pick_sound = pygame.mixer.Sound('sounds/pick.wav')

kiki_sounds['shot'].set_volume(0.5)
kiki_sounds['phrases'][0].set_volume(1.5)
kiki_sounds['phrases'][1].set_volume(1.5)

