import pygame
import Constants
import Images

screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption('Warriors')


def display_heals(hearts, line):
    for i, heart in enumerate(hearts):
        screen.blit(heart, (i * Constants.GAP_BETWEEN_HEARTS + Constants.HEART_INDENT, line))


def display_ammo(ammo, line):
    number = 0
    for i in range(ammo):
        screen.blit(Images.full_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
        number += 1
    for i in range(5 - number):
        screen.blit(Images.empty_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
        number += 1


def display_bullet_explosion(lifetime, x, y):
    screen.blit(Images.bullet_explosion_images[lifetime // 3], (x, y))


