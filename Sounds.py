import pygame as pg

pg.mixer.init()
hit_sound = pg.mixer.Sound('sounds/hit.wav')
shot_sound = pg.mixer.Sound('sounds/shoot.wav')
explosion_sound = pg.mixer.Sound('sounds/explosion.wav')

win_sound = pg.mixer.Sound('sounds/win.wav')
switch_sound = pg.mixer.Sound('sounds/switch.wav')
pick_sound = pg.mixer.Sound('sounds/pick.wav')

laser_sound = pg.mixer.Sound('sounds/laser_sound.wav')
laser_damage_sound = pg.mixer.Sound('sounds/laser_hit.wav')

laser_sound.set_volume(1.5)
