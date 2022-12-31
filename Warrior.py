import Sounds
from Inner import *
from Bullet import *
import Constants

class Warrior(pygame.sprite.Sprite):
    def __init__(self, game_side: str):
        super().__init__()

        self.hearts = [Images.full_heart, Images.full_heart, Images.full_heart]

        if game_side == 'top':
            self.borders = {'top': 159, 'bottom': 341, 'right': 512 - 9, 'left': 9}
            self.control_buttons = {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a,
                                    'right': pygame.K_d, 'fire': pygame.K_g}
            self.stats_line_level = Constants.TOP_LINE
            self.is_top_side = True

            self.image = pygame.image.load('images/blue_warrior.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=(100, 200))
        elif game_side == 'bottom':
            self.borders = {'top': 351, 'bottom': 533, 'right': 512 - 9, 'left': 9}
            self.control_buttons = {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT,
                                    'right': pygame.K_RIGHT, 'fire': pygame.K_RCTRL}
            self.stats_line_level = Constants.BOTTOM_LINE
            self.is_top_side = False

            self.image = pygame.image.load('images/red_warrior.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=(100, 400))
        else:
            print('Ошибка: неверно указан параметр game_side, при создании объекта класса Warrior. (top/bottom)')
            exit()

        # Задержка между выстрелами
        self.fire_delay = 0

        # Задержка между выстрелами и перезарядкой
        # (Чтобы началась перезарядка, нужно подождать, не стреляя)
        self.reload_delay = 0

        # Перезарядка патрон
        self.ammo_reload = 0

        self.speed = 2
        self.heals = 3
        self.ammo = 5

        self.isAlive = True

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

        if not self.fire_delay and self.ammo:
            if keys[self.control_buttons['fire']]:

                self.ammo -= 1
                Sounds.shoot_sound.play()
                self.fire_delay = 10
                self.reload_delay = 10

                if self.is_top_side:
                    blue_bullets_group.add(BlueBullet(self.rect.x, self.rect.y))
                else:
                    red_bullets_group.add(RedBullet(self.rect.x, self.rect.y))

    def do_damage(self):
        if self.is_top_side:
            for _ in red_hit_bullets:
                self.heals -= 1
                self.hearts.append(Images.empty_heart)
                self.hearts.pop(0)
        else:
            for _ in blue_hit_bullets:
                self.heals -= 1
                self.hearts.append(Images.empty_heart)
                self.hearts.pop(0)

    def display_heals(self):
        for i, heart in enumerate(self.hearts):
            Images.screen.blit(heart, (i * Constants.GAP_BETWEEN_HEARTS + Constants.HEART_INDENT, self.stats_line_level))

    def display_bullets(self):
        number = 0
        for i in range(self.ammo):
            Images.screen.blit(Images.full_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, self.stats_line_level))
            number += 1
        for i in range(5 - number):
            Images.screen.blit(Images.empty_bullet, (number * Constants.GAP_BETWEEN_BULLETS + Constants.BULLET_INDENT, self.stats_line_level))
            number += 1

    def reload(self):

        # Проверка на то, что выдержана задержка между выстрелом и перезарядкой
        if self.reload_delay:
            self.reload_delay -= 1
        else:

            # Проверка на то, что патрон меньше 5
            if self.ammo < 5:

                # Перезарядка
                self.ammo_reload += 1

                # Увеличение патрон, если перезарядка на нужном уровне
                if self.ammo_reload >= 30:
                    self.ammo += 1
                    self.ammo_reload = 0

    def update(self):
        if self.isAlive:
            self.warrior_control()
            self.reload()

        self.display_bullets()
        self.display_heals()

        if self.fire_delay:
            self.fire_delay -= 1