import pygame as pg
import Constants


class Visual:
    def __init__(self):
        self.screen = pg.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
        pg.display.set_caption('Warriors')
        pg.font.init()

        self.battlefield = pg.image.load('./images/scene/battlefield2.png').convert_alpha()
        self.choosing_field = pg.image.load('./images/choosing_field.png').convert_alpha()

        self.blue_wins = pg.image.load('./images/blue_wins.png').convert_alpha()
        self.red_wins = pg.image.load('./images/red_wins.png').convert_alpha()

        self.full_bullet = pg.image.load('./images/scene/full_bullet_2.png').convert_alpha()
        self.empty_bullet = pg.image.load('./images/scene/empty_bullet_2.png').convert_alpha()

        self.chosen_frame = pg.image.load('./images/chosen_frame.png').convert_alpha()
        self.empty_frame = pg.image.load('./images/empty_frame.png').convert_alpha()

        bullet_explosion_frame1 = pg.image.load('./images/bullet_explosion_animation/frame1.png').convert_alpha()
        bullet_explosion_frame2 = pg.image.load('./images/bullet_explosion_animation/frame2.png').convert_alpha()
        bullet_explosion_frame3 = pg.image.load('./images/bullet_explosion_animation/frame3.png').convert_alpha()
        bullet_explosion_images = (bullet_explosion_frame1,
                                   bullet_explosion_frame2,
                                   bullet_explosion_frame3,
                                   bullet_explosion_frame2,
                                   bullet_explosion_frame1)

        player_explosion_frame1 = pg.image.load('./images/player_explosion_animation/frame1.png').convert_alpha()
        player_explosion_frame2 = pg.image.load('./images/player_explosion_animation/frame2.png').convert_alpha()
        player_explosion_frame4 = pg.image.load('./images/player_explosion_animation/frame4.png').convert_alpha()
        player_explosion_frame5 = pg.image.load('./images/player_explosion_animation/frame5.png').convert_alpha()
        player_explosion_frame6 = pg.image.load('./images/player_explosion_animation/frame6.png').convert_alpha()
        player_explosion_images = [player_explosion_frame1,
                                   player_explosion_frame2,
                                   player_explosion_frame1,
                                   player_explosion_frame4,
                                   player_explosion_frame5,
                                   player_explosion_frame6]

        self.bullet_explosion_images = [pg.transform.scale2x(im) for im in bullet_explosion_images]
        self.player_explosion_images = [pg.transform.scale2x(im) for im in player_explosion_images]

        self.red_bullet = pg.image.load('./images/scene/red_bullet.png').convert_alpha()
        self.blue_bullet = pg.image.load('./images/scene/blue_bullet.png').convert_alpha()

        self.pixel_font = pg.font.Font('./font/Pixeltype.ttf', 100)

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

        self.win_fount = pg.font.Font('./font/SFPixelate-Bold.ttf', 150)

        self.empty_nickname_frame = pg.image.load('./images/empty_nickname_frame.png').convert_alpha()
        self.chosen_nickname_frame = pg.image.load('./images/chosen_nickname_frame.png').convert_alpha()

        self.laser_on_player = pg.image.load('./images/player_to_laser.png').convert_alpha()

        self.laser_animation = [pg.image.load('./images/laser_animation/blue_active_laser/frame0.png').convert_alpha(),
                                pg.image.load('./images/laser_animation/blue_active_laser/frame1.png').convert_alpha(),
                                pg.image.load('./images/laser_animation/blue_active_laser/frame2.png').convert_alpha(),
                                pg.image.load('./images/laser_animation/blue_active_laser/frame3.png').convert_alpha(),
                                pg.image.load('./images/laser_animation/blue_active_laser/frame4.png').convert_alpha(),
                                pg.image.load('./images/laser_animation/blue_active_laser/frame5.png').convert_alpha(),
                                pg.image.load('./images/laser_animation/blue_active_laser/frame6.png').convert_alpha()]

        self.laser_melting_stage_1 = \
            [pg.image.load('./images/laser_animation/laser_melting/stage_1/frame0.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_1/frame1.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_1/frame3.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_1/frame4.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_1/frame5.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_1/frame6.png').convert_alpha()]

        self.laser_melting_stage_2 = \
            [pg.image.load('./images/laser_animation/laser_melting/stage_2/frame0.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_2/frame1.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_2/frame3.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_2/frame4.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_2/frame5.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_2/frame6.png').convert_alpha()]

        self.laser_melting_stage_3 = \
            [pg.image.load('./images/laser_animation/laser_melting/stage_3/frame0.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_3/frame1.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_3/frame2.png').convert_alpha(),
             pg.image.load('./images/laser_animation/laser_melting/stage_3/frame3.png').convert_alpha()]

        self.laser_explosion_animation = [pg.image.load(
            './images/laser_explosion_animation/frame0.png').convert_alpha(),
                                          pg.image.load(
                                              './images/laser_explosion_animation/frame1.png').convert_alpha(),
                                          pg.image.load(
                                              './images/laser_explosion_animation/frame2.png').convert_alpha(),
                                          pg.image.load(
                                              './images/laser_explosion_animation/frame3.png').convert_alpha(),
                                          pg.image.load(
                                              './images/laser_explosion_animation/frame4.png').convert_alpha(),
                                          pg.image.load(
                                              './images/laser_explosion_animation/frame5.png').convert_alpha()]

        self.test_image = pg.image.load('./images/test3.png').convert_alpha()
        self.red_health_point = pg.image.load('./images/red_health_point2.png').convert_alpha()
        self.yellow_health_point = pg.image.load('./images/yellow_health_point.png').convert_alpha()
        self.green_health_point = pg.image.load('./images/green_health_point2.png').convert_alpha()
        self.heart = pg.image.load('./images/heart.png').convert_alpha()

        self.gunslider_warrior = {'top': pg.image.load('./images/warriors/blue_gunslider_warrior.png').convert_alpha(),
                                  'bottom': pg.image.load(
                                      './images/warriors/red_gunslider_warrior.png').convert_alpha()}

        self.laser_warrior = {'top': pg.image.load('./images/warriors/blue_laser_warrior.png').convert_alpha(),
                                  'bottom': pg.image.load('./images/warriors/red_laser_warrior.png').convert_alpha()}

        self.machinegun_warrior = {'top': pg.image.load('./images/warriors/blue_machinegun.png').convert_alpha(),
                                   'bottom': pg.image.load('./images/warriors/red_machingun.png').convert_alpha()}

        self.komar_warrior = {'top': pg.image.load('./images/warriors/blue_komar.png').convert_alpha(),
                                  'bottom': pg.image.load('./images/warriors/red_komar.png').convert_alpha()}

        self.warriors_textures = [self.gunslider_warrior, self.laser_warrior, self.komar_warrior,
                                  self.machinegun_warrior, self.gunslider_warrior]

        self.red_sting = pg.image.load('./images/red_sting_2.png').convert_alpha()
        self.blue_sting = pg.image.load('./images/blue_sting.png').convert_alpha()

        self.red_pellet = pg.image.load('./images/red_pellet.png').convert_alpha()
        self.blue_pellet = pg.image.load('./images/blue_pellet.png').convert_alpha()
