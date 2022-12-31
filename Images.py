import pygame

battlefield = pygame.image.load('images/battlefield2.png').convert_alpha()
blue_wins_background = pygame.image.load('images/blue_wins_screen.png').convert_alpha()
red_wins_background = pygame.image.load('images/red_wins_screen.png').convert_alpha()

full_heart = pygame.image.load('images/full_heart.png').convert_alpha()
empty_heart = pygame.image.load('images/empty_heart.png').convert_alpha()

full_bullet = pygame.image.load('images/full_bullet_2.png')
empty_bullet = pygame.image.load('images/empty_bullet_2.png').convert_alpha()

bullet_explosion_frame1 = pygame.image.load('images/bullet_explosion_animation/frame1.png').convert_alpha()
bullet_explosion_frame2 = pygame.image.load('images/bullet_explosion_animation/frame2.png').convert_alpha()
bullet_explosion_frame3 = pygame.image.load('images/bullet_explosion_animation/frame3.png').convert_alpha()
bullet_explosion_images = (bullet_explosion_frame1,
                           bullet_explosion_frame2,
                           bullet_explosion_frame3,
                           bullet_explosion_frame2,
                           bullet_explosion_frame1)

player_explosion_frame1 = pygame.image.load('images/player_explosion_animation/frame1.png').convert_alpha()
player_explosion_frame2 = pygame.image.load('images/player_explosion_animation/frame2.png').convert_alpha()
player_explosion_frame4 = pygame.image.load('images/player_explosion_animation/frame4.png').convert_alpha()
player_explosion_frame5 = pygame.image.load('images/player_explosion_animation/frame5.png').convert_alpha()
player_explosion_frame6 = pygame.image.load('images/player_explosion_animation/frame6.png').convert_alpha()
player_explosion_images = [player_explosion_frame1,
                           player_explosion_frame2,
                           player_explosion_frame1,
                           player_explosion_frame4,
                           player_explosion_frame5,
                           player_explosion_frame6]

red_bullet = pygame.image.load('images/red_bullet.png').convert_alpha()
blue_bullet = pygame.image.load('images/blue_bullet.png').convert_alpha()
