import pygame
import Constants

screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption('Warriors')


def display_character_frames(line, pointer):
    for i in range(5):
        if i == pointer:
            screen.blit(chosen_frame, (i * Constants.GAP_BETWEEN_FRAMES + Constants.FRAME_INDENT, line))
        else:
            screen.blit(empty_frame, (i * Constants.GAP_BETWEEN_FRAMES + Constants.FRAME_INDENT, line))

        screen.blit(family[i], (i * Constants.GAP_BETWEEN_FRAMES + 46, line + 25))


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


def display_picking_character_name(pointer, line, isPicked):
    if isPicked:
        screen.blit(chosen_nickname_frame, (Constants.NICKNAME_FRAME_INDENT, line))
        if pointer == 1:
            screen.blit(green_family_nicknames[pointer], (Constants.NICKNAME_INDENT + 32, line + 22))
        else:
            screen.blit(green_family_nicknames[pointer], (Constants.NICKNAME_INDENT, line + 22))

    else:
        screen.blit(empty_nickname_frame, (Constants.NICKNAME_FRAME_INDENT, line))
        if pointer == 1:
            screen.blit(family_nicknames[pointer], (Constants.NICKNAME_INDENT + 32, line + 22))
        else:
            screen.blit(family_nicknames[pointer], (Constants.NICKNAME_INDENT, line + 22))


battlefield = pygame.image.load('images/scene/battlefield2.png').convert_alpha()
choosing_field = pygame.image.load('images/choosing_field.png').convert_alpha()

blue_wins_background = pygame.image.load('images/scene/blue_wins_screen.png').convert_alpha()
red_wins_background = pygame.image.load('images/scene/red_wins_screen.png').convert_alpha()

full_heart = pygame.image.load('images/scene/full_heart.png').convert_alpha()
empty_heart = pygame.image.load('images/scene/empty_heart.png').convert_alpha()

full_bullet = pygame.image.load('images/scene/full_bullet_2.png')
empty_bullet = pygame.image.load('images/scene/empty_bullet_2.png').convert_alpha()

chosen_frame = pygame.image.load('images/chosen_frame.png').convert_alpha()
empty_frame = pygame.image.load('images/empty_frame.png').convert_alpha()

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

dada = pygame.image.load('images/family_warriors/dada.png').convert_alpha()
kiki = pygame.image.load('images/family_warriors/kiki.png').convert_alpha()
vava = pygame.image.load('images/family_warriors/dummy.png').convert_alpha()
papa = pygame.image.load('images/family_warriors/dummy.png').convert_alpha()
mama = pygame.image.load('images/family_warriors/dummy.png').convert_alpha()

family = [dada, kiki, vava, papa, mama]

pygame.font.init()

pixel_font = pygame.font.Font('font/Pixeltype.ttf',100)

dada_nickname = pixel_font.render('dada', False, (0, 0, 0))
kiki_nickname = pixel_font.render('kiki', False, (0, 0, 0))
vava_nickname = pixel_font.render('vava', False, (0, 0, 0))
papa_nickname = pixel_font.render('papa', False, (0, 0, 0))
mama_nickname = pixel_font.render('mama', False, (0, 0, 0))

green_dada_nickname = pixel_font.render('dada', False, (10, 100, 10))
green_kiki_nickname = pixel_font.render('kiki', False, (10, 100, 10))
green_vava_nickname = pixel_font.render('vava', False, (10, 100, 10))
green_papa_nickname = pixel_font.render('papa', False, (10, 100, 10))
green_mama_nickname = pixel_font.render('mama', False, (10, 100, 10))

green_family_nicknames = [green_dada_nickname, green_kiki_nickname, green_vava_nickname,
                          green_papa_nickname, green_mama_nickname]

family_nicknames = [dada_nickname, kiki_nickname, vava_nickname, papa_nickname, mama_nickname]

empty_nickname_frame = pygame.image.load('images/empty_nickname_frame.png').convert_alpha()
chosen_nickname_frame = pygame.image.load('images/chosen_nickname_frame.png').convert_alpha()
