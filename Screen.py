import pygame as pg
import Constants

class Screen:
    def __init__(self):
        self.screen = pg.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
        pg.display.set_caption('Warriors')

        self.battlefield = pg.image.load('images/scene/battlefield2.png').convert_alpha()
        self.choosing_field = pg.image.load('images/choosing_field.png').convert_alpha()

        self.blue_wins = pg.image.load('images/blue_wins.png').convert_alpha()
        self.red_wins = pg.image.load('images/red_wins.png').convert_alpha()

        self.full_heart = pg.image.load('images/scene/full_heart.png').convert_alpha()
        self.empty_heart = pg.image.load('images/scene/empty_heart.png').convert_alpha()

        self.full_bullet = pg.image.load('images/scene/full_bullet_2.png')
        self.empty_bullet = pg.image.load('images/scene/empty_bullet_2.png').convert_alpha()

        self.chosen_frame = pg.image.load('images/chosen_frame.png').convert_alpha()
        self.empty_frame = pg.image.load('images/empty_frame.png').convert_alpha()

        bullet_explosion_frame1 = pg.image.load('images/bullet_explosion_animation/frame1.png').convert_alpha()
        bullet_explosion_frame2 = pg.image.load('images/bullet_explosion_animation/frame2.png').convert_alpha()
        bullet_explosion_frame3 = pg.image.load('images/bullet_explosion_animation/frame3.png').convert_alpha()
        bullet_explosion_images = (bullet_explosion_frame1,
                                   bullet_explosion_frame2,
                                   bullet_explosion_frame3,
                                   bullet_explosion_frame2,
                                   bullet_explosion_frame1)

        player_explosion_frame1 = pg.image.load('images/player_explosion_animation/frame1.png').convert_alpha()
        player_explosion_frame2 = pg.image.load('images/player_explosion_animation/frame2.png').convert_alpha()
        player_explosion_frame4 = pg.image.load('images/player_explosion_animation/frame4.png').convert_alpha()
        player_explosion_frame5 = pg.image.load('images/player_explosion_animation/frame5.png').convert_alpha()
        player_explosion_frame6 = pg.image.load('images/player_explosion_animation/frame6.png').convert_alpha()
        player_explosion_images = [player_explosion_frame1,
                                   player_explosion_frame2,
                                   player_explosion_frame1,
                                   player_explosion_frame4,
                                   player_explosion_frame5,
                                   player_explosion_frame6]

        self.bullet_explosion_images = [pg.transform.scale2x(im) for im in bullet_explosion_images]
        self.player_explosion_images = [pg.transform.scale2x(im) for im in player_explosion_images]

        self.red_bullet = pg.image.load('images/scene/red_bullet.png').convert_alpha()
        self.blue_bullet = pg.image.load('images/scene/blue_bullet.png').convert_alpha()

        self.dada = pg.image.load('images/family_warriors/red.png').convert_alpha()
        self.kiki = pg.image.load('images/family_warriors/blue.png').convert_alpha()
        self.vava = pg.image.load('images/family_warriors/green.png').convert_alpha()
        self.papa = pg.image.load('images/family_warriors/yellow.png').convert_alpha()
        self.mama = pg.image.load('images/family_warriors/purple.png').convert_alpha()

        self.family = [self.dada, self.kiki, self.vava, self.papa, self.mama]

        pg.font.init()

        self.pixel_font = pg.font.Font('font/Pixeltype.ttf', 100)

        dada_nickname = self.pixel_font.render('dada', False, Constants.BLACK)
        kiki_nickname = self.pixel_font.render('kiki', False, Constants.BLACK)
        vava_nickname = self.pixel_font.render('vava', False, Constants.BLACK)
        papa_nickname = self.pixel_font.render('papa', False, Constants.BLACK)
        mama_nickname = self.pixel_font.render('mama', False, Constants.BLACK)

        green_dada_nickname = self.pixel_font.render('dada', False, Constants.DARK_GREEN)
        green_kiki_nickname = self.pixel_font.render('kiki', False, Constants.DARK_GREEN)
        green_vava_nickname = self.pixel_font.render('vava', False, Constants.DARK_GREEN)
        green_papa_nickname = self.pixel_font.render('papa', False, Constants.DARK_GREEN)
        green_mama_nickname = self.pixel_font.render('mama', False, Constants.DARK_GREEN)

        self.green_family_nicknames = [green_dada_nickname, green_kiki_nickname, green_vava_nickname,
                                  green_papa_nickname, green_mama_nickname]

        self.family_nicknames = [dada_nickname, kiki_nickname, vava_nickname, papa_nickname, mama_nickname]

        self.win_fount = pg.font.Font('font/SFPixelate-Bold.ttf', 150)
        self.names = ['dada', 'kiki', 'vava', 'papa', 'mama']

        self.empty_nickname_frame = pg.image.load('images/empty_nickname_frame.png').convert_alpha()
        self.chosen_nickname_frame = pg.image.load('images/chosen_nickname_frame.png').convert_alpha()

    def display_character_frames(self, line, pointer):
        for i in range(5):
            if i == pointer:
                self.screen.blit(self.chosen_frame, (i * Constants.GAP_BETWEEN_FRAMES + Constants.FRAME_INDENT, line))
            else:
                self.screen.blit(self.empty_frame, (i * Constants.GAP_BETWEEN_FRAMES + Constants.FRAME_INDENT, line))

            self.screen.blit(self.family[i], (i * Constants.GAP_BETWEEN_FRAMES + 46, line + 25))


    def display_heals(self, hearts, line):
        for i, heart in enumerate(hearts):
            self.screen.blit(heart, (i * Constants.GAP_BETWEEN_HEARTS + Constants.HEART_INDENT, line))


    def display_ammo(self, ammo, line):
        number = 0
        for i in range(ammo):
            self.screen.blit(self.full_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
            number += 1
        for i in range(5 - number):
            self.screen.blit(self.empty_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
            number += 1


    def display_bullet_explosion(self, lifetime, x, y):
        self.screen.blit(self.bullet_explosion_images[lifetime // 3], (x - 5, y - 5))


    def display_player_explosion(self, lifetime, x, y):
        self.screen.blit(self.player_explosion_images[lifetime // 5], (x - 16, y - 16))


    def display_picking_character_name(self, pointer, line, isPicked):
        if isPicked:
            self.screen.blit(self.chosen_nickname_frame, (Constants.NICKNAME_FRAME_INDENT, line))
            if pointer == 1:
                self.screen.blit(self.green_family_nicknames[pointer], (Constants.NICKNAME_INDENT + 32, line + 22))
            else:
                self.screen.blit(self.green_family_nicknames[pointer], (Constants.NICKNAME_INDENT, line + 22))

        else:
            self.screen.blit(self.empty_nickname_frame, (Constants.NICKNAME_FRAME_INDENT, line))
            if pointer == 1:
                self.screen.blit(self.family_nicknames[pointer], (Constants.NICKNAME_INDENT + 32, line + 22))
            else:
                self.screen.blit(self.family_nicknames[pointer], (Constants.NICKNAME_INDENT, line + 22))
