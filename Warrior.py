import pygame
import Constants
import Sounds
from Arsenal import LaserGun, GunBullet
from Animations import PlayerExplosion


class BaseWarrior(pygame.sprite.Sprite):
    def __init__(self, game_side, visual, health):
        super().__init__()

        if game_side == 'top':
            self.borders = {'top': 159, 'bottom': 341, 'right': 512 - 9, 'left': 9}
            self.control_buttons = {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a,
                                    'right': pygame.K_d, 'fire': pygame.K_g}

            self.stats_line_level = Constants.TOP_STAT_LINE

            self.is_top_side = True
            self.start_x = 100
            self.start_y = 250

        elif game_side == 'bottom':
            self.borders = {'top': 351, 'bottom': 533, 'right': 512 - 9, 'left': 9}
            self.control_buttons = {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT,
                                    'right': pygame.K_RIGHT, 'fire': pygame.K_RCTRL}

            self.stats_line_level = Constants.BOTTOM_STAT_LINE
            self.is_top_side = False
            self.start_x = Constants.WIDTH - 100
            self.start_y = 542 - 100

        self.speed = 3
        self.health = health
        self.current_health = self.health
        self.isAlive = True
        self.visual = visual
        self.death_played = False

    def control(self):
        keys = pygame.key.get_pressed()

        if keys[self.control_buttons['up']] and self.rect.top > self.borders['top']:
            self.rect.y -= self.speed
        if keys[self.control_buttons['down']] and self.rect.bottom < self.borders['bottom']:
            self.rect.y += self.speed
        if keys[self.control_buttons['left']] and self.rect.left > self.borders['left']:
            self.rect.x -= self.speed
        if keys[self.control_buttons['right']] and self.rect.right < self.borders['right']:
            self.rect.x += self.speed

    def display_heals(self):
        if self.is_top_side:
            x = Constants.TOP_HEALTH_BAR_X
            y = Constants.TOP_HEALTH_BAR_Y
        else:
            x = Constants.BOTTOM_HEALTH_BAR_X
            y = Constants.BOTTOM_HEALTH_BAR_Y

        hp_percent = self.current_health / self.health
        if hp_percent <= 0.2:
            point = self.visual.red_health_point
        elif hp_percent <= 0.5:
            point = self.visual.yellow_health_point
        else:
            point = self.visual.green_health_point

        health_points = int (hp_percent * 43)

        for i in range(health_points):
            self.visual.screen.blit(point, (x + (i + 1)*4, y + 4))

        self.visual.screen.blit(self.visual.test_image, (x, y))
        self.visual.screen.blit(self.visual.heart, (x - 20, y - 8))

    def display_ammo(self, ammo, line):
        number = 0
        for i in range(ammo):
            self.visual.screen.blit(self.visual.full_bullet,
                                    (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
            number += 1
        for i in range(5 - number):
            self.visual.screen.blit(self.visual.empty_bullet,
                                    (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, line))
            number += 1

    def get_damage(self, damage):
        self.current_health -= damage

    def death(self, animations):
        Sounds.explosion_sound.play()
        animations.append(PlayerExplosion(self.rect.x + 16, self.rect.y + 16))
        self.rect.x = 512
        self.rect.y = 512
        self.isAlive = False
        self.death_played = True


class Gunslinger(BaseWarrior):
    def __init__(self, game_side, visual):
        super().__init__(game_side, visual, 200)

        self.image = visual.gunslider_warrior[game_side]

        self.shot_sound = Sounds.shot_sound

        self.rect = self.image.get_rect(topleft=(self.start_x, self.start_y))

        # Задержка между выстрелами
        self.fire_delay = 10

        # Задержка между выстрелами и перезарядкой
        # (Чтобы началась перезарядка, нужно подождать, не стреляя)
        self.reload_delay = 10

        # Скорость перезарядки (больше - медленнее перезарядка)
        self.ammo_reload = 30

        self.bullet_speed = 8

        self.ammo = 5
        self.damage = 45

        self.fire_delay_level = 0
        self.reload_delay_level = 0
        self.ammo_reload_level = 0

        self.bullets_group = pygame.sprite.Group()

    def shooting(self):
        keys = pygame.key.get_pressed()

        if not self.fire_delay_level and self.ammo:
            if keys[self.control_buttons['fire']]:

                self.ammo -= 1
                self.shot_sound.play()
                self.fire_delay_level = self.fire_delay
                self.reload_delay_level = self.reload_delay

                # (+ 6) чтобы пуля выходила из середины игрока, иначе смещена влево
                self.bullets_group.add(GunBullet((self.rect.x + 6, self.rect.y),
                                                 self.is_top_side, self.visual, self.bullet_speed))

    def reload(self):

        # Проверка на то, что выдержана задержка между выстрелом и перезарядкой
        if self.reload_delay_level:
            self.reload_delay_level -= 1
        else:

            # Проверка на то, что патрон меньше 5
            if self.ammo < 5:

                # Перезарядка
                self.ammo_reload_level += 1

                # Увеличение патрон, если перезарядка на нужном уровне
                if self.ammo_reload_level >= self.ammo_reload:
                    self.ammo += 1
                    self.ammo_reload_level = 0

    def update(self, enemy, animations):
        if self.isAlive:
            self.control()
            self.reload()
            self.shooting()

        self.display_ammo(self.ammo, self.stats_line_level)
        self.display_heals()

        self.bullets_group.draw(self.visual.screen)
        self.bullets_group.update()

        hit_bullets = pygame.sprite.spritecollide(enemy, self.bullets_group, False)

        if hit_bullets:
            for bullet in hit_bullets:
                bullet.hit(animations, (enemy.health != 1))
                enemy.get_damage(self.damage)

        if self.current_health <= 0 and not self.death_played:
            self.death(animations)

        if self.fire_delay_level:
            self.fire_delay_level -= 1


class Laser(BaseWarrior):
    def __init__(self, game_side, visual):
        super().__init__(game_side, visual, 200)

        self.image = visual.laser_warrior[game_side]

        self.rect = self.image.get_rect(topleft=(self.start_x, self.start_y))

        self.speed = 3
        self.laser_gun = LaserGun(self, visual)
        self.damage = 2

        self.energy = 100
        self.energy_level = self.energy

        self.energy_reload_speed = 1
        self.laser_delay = 15
        self.laser_delay_level = 0

        if self.is_top_side:
            self.laser_sound = Sounds.laser_sound_1
            self.laser_damage_sound = Sounds.laser_damage_sound_1
        else:
            self.laser_sound = Sounds.laser_sound_2
            self.laser_damage_sound = Sounds.laser_damage_sound_2

    def reload(self):
        if not self.laser_gun.active:
            if self.energy_level < 100:
                self.energy_level += self.energy_reload_speed

            if self.laser_delay_level:
                self.laser_delay_level -= 1

            # print(self.laser_delay_level)

    def laser_control(self, enemy, animations):
        keys = pygame.key.get_pressed()

        if keys[self.control_buttons['fire']] and self.energy_level and not self.laser_delay_level:
            enemy_front = enemy.rect.top if self.is_top_side else enemy.rect.bottom

            self.energy_level -= 1

            hit = self.laser_gun.activate(enemy.rect.left, enemy.rect.right, enemy_front)
            if hit:
                enemy.get_damage(self.damage)

        else:
            if self.laser_gun.active:
                self.laser_delay_level = self.laser_delay

            self.laser_gun.melt_laser(animations)

    def update(self, enemy, animations):
        if self.isAlive:
            self.control()
            self.laser_control(enemy, animations)
            self.reload()

        _bullets_ = int ((self.energy_level / self.energy) * 5)

        self.display_ammo(_bullets_, self.stats_line_level)
        self.display_heals()

        if self.current_health <= 0 and not self.death_played:
            self.laser_gun.stop_playing_sounds()
            self.death(animations)
