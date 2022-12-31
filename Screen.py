import pygame
import Constants

screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption('Warriors')


def display_heals(hearts, line):
    for i, heart in enumerate(hearts):
        screen.blit(heart, (i * Constants.GAP_BETWEEN_HEARTS + Constants.HEART_INDENT, line))


def display_ammo(ammo, line):
    number = 0
    for i in range(ammo):
        screen.blit(full_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
        number += 1
    for i in range(5 - number):
        screen.blit(empty_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
        number += 1


def display_bullet_explosion(lifetime, x, y):
    screen.blit(bullet_explosion_images[lifetime // 3], (x - 5, y - 5))


def display_player_explosion(lifetime, x, y):
    screen.blit(player_explosion_images[lifetime // 5], (x - 16, y - 16))


battlefield = pygame.image.load('images/scene/battlefield2.png').convert_alpha()
blue_wins_background = pygame.image.load('images/scene/blue_wins_screen.png').convert_alpha()
red_wins_background = pygame.image.load('images/scene/red_wins_screen.png').convert_alpha()

full_heart = pygame.image.load('images/scene/full_heart.png').convert_alpha()
empty_heart = pygame.image.load('images/scene/empty_heart.png').convert_alpha()

full_bullet = pygame.image.load('images/scene/full_bullet_2.png')
empty_bullet = pygame.image.load('images/scene/empty_bullet_2.png').convert_alpha()

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

bullet_explosion_images = [pygame.transform.scale2x(im) for im in bullet_explosion_images]
player_explosion_images = [pygame.transform.scale2x(im) for im in player_explosion_images]

red_bullet = pygame.image.load('images/scene/red_bullet.png').convert_alpha()
blue_bullet = pygame.image.load('images/scene/blue_bullet.png').convert_alpha()
