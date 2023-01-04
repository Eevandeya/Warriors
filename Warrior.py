import pygame
import Constants
import Sounds
from Arsenal import LaserGun, GunBullet
from Animations import PlayerExplosion


class BaseWarrior(pygame.sprite.Sprite):
    def __init__(self, game_side, visual):
        super().__init__()

        self.hearts = [visual.full_heart, visual.full_heart, visual.full_heart]
        self.empty_heart = visual.empty_heart

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
        self.health = 3
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

    def display_heals(self, hearts, line):
        for i, heart in enumerate(hearts):
            self.visual.screen.blit(heart, (i * Constants.GAP_BETWEEN_HEARTS + Constants.HEART_INDENT, line))

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
        self.health -= damage
        self.hearts.append(self.empty_heart)
        self.hearts.pop(0)

    def death(self, animations):
        Sounds.explosion_sound.play()
        animations.append(PlayerExplosion(self.rect.x + 16, self.rect.y + 16))
        self.rect.x = 500
        self.rect.y = 500
        self.isAlive = False
        self.death_played = True


class Gunslinger(BaseWarrior):
    def __init__(self, game_side, character, visual):
        super().__init__(game_side, visual)
        self.health = 30

        self.character = character
        self.image = visual.family[character]

        self.hit_sound = Sounds.hit_sound
        self.shot_sound = Sounds.shot_sound
        self.death_sound = Sounds.explosion_sound

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
        self.damage = 1

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
        self.display_heals(self.hearts, self.stats_line_level)

        self.bullets_group.draw(self.visual.screen)
        self.bullets_group.update()

        hit_bullets = pygame.sprite.spritecollide(enemy, self.bullets_group, False)

        if hit_bullets:
            for bullet in hit_bullets:
                bullet.hit(animations, (enemy.health != 1))
                enemy.get_damage(1)

        if self.health <= 0 and not self.death_played:
            self.death(animations)

        if self.fire_delay_level:
            self.fire_delay_level -= 1


class Laser(BaseWarrior):
    def __init__(self, game_side, character, visual):
        super().__init__(game_side, visual)

        self.hearts = [visual.full_heart, visual.full_heart, visual.full_heart]
        self.empty_heart = visual.empty_heart

        self.character = character
        self.image = visual.family[character]

        self.hit_sound = Sounds.hit_sound
        self.shot_sound = Sounds.shot_sound
        self.death_sound = Sounds.explosion_sound

        self.rect = self.image.get_rect(topleft=(self.start_x, self.start_y))

        self.speed = 3
        self.heals = 3
        self.laser_gun = LaserGun(self, visual)
        self.damage = 1

    def activate_laser(self, enemy, animations):
        keys = pygame.key.get_pressed()

        if keys[self.control_buttons['fire']]:

            if not self.is_top_side:
                hit = self.laser_gun.activate(enemy.rect.left, enemy.rect.right, enemy.rect.bottom)
                if hit:
                    enemy.get_damage(self.damage)

        else:
            self.laser_gun.melt_laser(animations)

    def update(self, enemy, animations):
        if self.isAlive:
            self.control()
            self.activate_laser(enemy, animations)

        self.display_ammo(5, self.stats_line_level)
        self.display_heals(self.hearts, self.stats_line_level)

        if self.health <= 0 and not self.death_played:
            self.laser_gun.stop_playing_sounds()
            self.death(animations)
