import pygame
import Constants
import Sounds
from Screen import display_heals, display_ammo, full_heart, empty_heart, family

class Warrior(pygame.sprite.Sprite):
    def __init__(self, game_side, character):
        super().__init__()

        self.hearts = [full_heart, full_heart, full_heart]

        self.character = character
        self.image = family[character]

        self.hit_sound = Sounds.hit_sound
        self.shot_sound = Sounds.shot_sound
        self.death_sound = Sounds.explosion_sound

        if game_side == 'top':
            self.borders = {'top': 159, 'bottom': 341, 'right': 512 - 9, 'left': 9}
            self.control_buttons = {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a,
                                    'right': pygame.K_d, 'fire': pygame.K_g}

            self.stats_line_level = Constants.TOP_STAT_LINE
            self.is_top_side = True

            self.rect = self.image.get_rect(topleft=(100, 250))

        elif game_side == 'bottom':
            self.borders = {'top': 351, 'bottom': 533, 'right': 512 - 9, 'left': 9}
            self.control_buttons = {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT,
                                    'right': pygame.K_RIGHT, 'fire': pygame.K_RCTRL}

            self.stats_line_level = Constants.BOTTOM_STAT_LINE
            self.is_top_side = False

            self.rect = self.image.get_rect(topleft=(Constants.WIDTH - 100, 542 - 100))

        else:
            print('Ошибка: неверно указан параметр game_side, при создании объекта класса Warrior. (top/bottom)')
            exit()

        """Настраиваемые параметры"""
        # Задержка между выстрелами
        self.fire_delay = 10

        # Задержка между выстрелами и перезарядкой
        # (Чтобы началась перезарядка, нужно подождать, не стреляя)
        self.reload_delay = 10

        # Скорость перезарядки (больше - медленнее перезарядка)
        self.ammo_reload = 30

        self.speed = 3
        self.heals = 3
        self.ammo = 5
        """==========================="""

        self.isAlive = True
        self.fire_delay_level = 0
        self.reload_delay_level = 0
        self.ammo_reload_level = 0

    def warrior_control(self):
        keys = pygame.key.get_pressed()

        if keys[self.control_buttons['up']] and self.rect.top > self.borders['top']:
            self.rect.y -= self.speed
        if keys[self.control_buttons['down']] and self.rect.bottom < self.borders['bottom']:
            self.rect.y += self.speed
        if keys[self.control_buttons['left']] and self.rect.left > self.borders['left']:
            self.rect.x -= self.speed
        if keys[self.control_buttons['right']] and self.rect.right < self.borders['right']:
            self.rect.x += self.speed

    def warrior_shots(self):
        keys = pygame.key.get_pressed()

        if not self.fire_delay_level and self.ammo:
            if keys[self.control_buttons['fire']]:

                self.ammo -= 1
                self.shot_sound.play()
                self.fire_delay_level = self.fire_delay
                self.reload_delay_level = self.reload_delay

                # (+ 6) чтобы пуля выходила из середины игрока, иначе смещена влево
                return self.rect.x + 6, self.rect.y
        return False

    def do_damage(self, bullets_num):
        for _ in range(bullets_num):
            self.heals -= 1
            self.hearts.append(empty_heart)
            self.hearts.pop(0)

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

    def update(self):
        if self.isAlive:
            self.warrior_control()
            self.reload()

        display_ammo(self.ammo, self.stats_line_level)
        display_heals(self.hearts, self.stats_line_level)

        if self.fire_delay_level:
            self.fire_delay_level -= 1
