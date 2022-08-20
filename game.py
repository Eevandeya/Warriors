import pygame


class BottomWarrior(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/red_warrior.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 400))

        self.hearts = [full_heart, full_heart, full_heart]
        self.bullets_list = [full_bullet for _ in range(5)]

    # Задержка между выстрелами
    fire_delay = 0

    # Задержка между выстрелами и перезарядкой
    # (Чтобы началась перезарядка, нужно подождать, не стреляя)
    reload_delay = 0

    # Перезарядка патрон
    ammo_reload = 0

    borders = {'top': 351, 'bottom': 533, 'right': 512 - 9, 'left': 9}
    speed = 2
    heals = 3
    ammo = 5

    def warrior_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.top > self.borders['top']:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.borders['bottom']:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > self.borders['left']:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.borders['right']:
            self.rect.x += self.speed

        if keys[pygame.K_RCTRL] and not self.fire_delay and self.ammo:
            self.ammo -= 1
            red_bullets_group.add(RedBullet(self.rect.x, self.rect.y))
            shoot_sound.play()
            self.fire_delay = 10
            self.reload_delay = 10

    def do_damage(self):
        for _ in blue_hit_bullets:
            self.heals -= 1
            self.hearts.append(empty_heart)
            self.hearts.pop(0)

    def display_heals(self):
        for i, heart in enumerate(self.hearts):
            screen.blit(heart, (i * gap_between_hearts + heart_indent, bottom_line))

    def display_bullets(self):
        number = 0
        for i in range(self.ammo):
            screen.blit(full_bullet, (number * gap_between_bullets + bullet_indent, bottom_line))
            number += 1
        for i in range(5 - number):
            screen.blit(empty_bullet, (number * gap_between_bullets + bullet_indent, bottom_line))
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
        self.warrior_control()
        self.display_heals()
        self.display_bullets()
        self.reload()

        if self.fire_delay:
            self.fire_delay -= 1


class RedBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_x, warrior_y):
        super().__init__()
        self.image = pygame.image.load('images/red_bullet.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def update(self):
        self.rect.y -= 6
        self.destroy()

    def destroy(self):
        if self.rect.y <= -30:
            self.kill()


class TopWarrior(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/blue_warrior.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 250))
        self.hearts = [full_heart, full_heart, full_heart]

    # Задержка между выстрелами
    fire_delay = 0

    # Задержка между выстрелами и перезарядкой
    # (Чтобы началась перезарядка, нужно подождать, не стреляя)
    reload_delay = 0

    # Перезарядка патрон
    ammo_reload = 0

    borders = {'top': 159, 'bottom': 341, 'right': 512 - 9, 'left': 9}
    speed = 2
    heals = 3
    ammo = 5

    def warrior_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.top > self.borders['top']:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < self.borders['bottom']:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > self.borders['left']:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < self.borders['right']:
            self.rect.x += self.speed

        if keys[pygame.K_g] and not self.fire_delay and self.ammo:
            blue_bullets_group.add(BlueBullet(self.rect.x, self.rect.y))
            self.ammo -= 1
            shoot_sound.play()
            self.fire_delay = 10
            self.reload_delay = 10

    def do_damage(self):
        for _ in red_hit_bullets:
            self.heals -= 1
            self.hearts.append(empty_heart)
            self.hearts.pop(0)

    def display_heals(self):
        for i, heart in enumerate(self.hearts):
            screen.blit(heart, (i * gap_between_hearts + heart_indent, top_line))

    def display_bullets(self):
        number = 0
        for i in range(self.ammo):
            screen.blit(full_bullet, (number * gap_between_bullets + bullet_indent, top_line))
            number += 1
        for i in range(5 - number):
            screen.blit(empty_bullet, (number * gap_between_bullets + bullet_indent, top_line))
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
        self.warrior_control()
        self.display_heals()
        self.display_bullets()
        self.reload()

        if self.fire_delay:
            self.fire_delay -= 1


class BlueBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_x, warrior_y):
        super().__init__()
        self.image = pygame.image.load('images/blue_bullet.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def update(self):
        self.rect.y += 6

    def destroy(self):
        if self.rect.y > 512 + 30:
            self.kill()


class Explosion:
    def __init__(self, x, y):
        self.x = x - 6
        self.y = y - 3
        self.lifetime = 0

    def update(self):
        if self.lifetime == 14:
            return True
        else:
            screen.blit(explosion_images[self.lifetime // 3], (self.x, self.y))
            self.lifetime += 1
            return False


def kill_bullet_and_spawn_explosion():
    for bullet in red_hit_bullets + blue_hit_bullets:
        explosions.append(Explosion(bullet.rect.x, bullet.rect.y))
        hit_sound.play()
        bullet.kill()


def update_explosions():
    for explosion in explosions:
        isdead = explosion.update()
        if isdead:
            explosions.remove(explosion)


pygame.init()

width = 512
height = 392 + 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

battlefield = pygame.image.load('images/battlefield2.png').convert_alpha()
full_heart = pygame.image.load('images/full_heart.png').convert_alpha()
empty_heart = pygame.image.load('images/empty_heart.png').convert_alpha()
full_bullet = pygame.image.load('images/full_bullet_2.png')
empty_bullet = pygame.image.load('images/empty_bullet_2.png').convert_alpha()

hit_sound = pygame.mixer.Sound('sounds/hit.wav')
shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')

explosion_frame1 = pygame.image.load('images/explosion_animation/frame1.png').convert_alpha()
explosion_frame2 = pygame.image.load('images/explosion_animation/frame2.png').convert_alpha()
explosion_frame3 = pygame.image.load('images/explosion_animation/frame3.png').convert_alpha()
explosion_images = (explosion_frame1, explosion_frame2, explosion_frame3, explosion_frame2, explosion_frame1)

hit_sound.set_volume(0.1)
shoot_sound.set_volume(0.1)

gap_between_hearts = 64
gap_between_bullets = 42

heart_indent = 20
bullet_indent = 270

top_line = 43
bottom_line = 585


screen.fill('#FFFFFF')


red_warrior_group = pygame.sprite.GroupSingle()
red_warrior_group.add(BottomWarrior())

blue_warrior_group = pygame.sprite.GroupSingle()
blue_warrior_group.add(TopWarrior())

red_bullets_group = pygame.sprite.Group()
blue_bullets_group = pygame.sprite.Group()
explosions = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('#dcdcdc')

    screen.blit(battlefield, (0, 150))

    red_bullets_group.draw(screen)
    red_bullets_group.update()

    blue_bullets_group.draw(screen)
    blue_bullets_group.update()

    red_warrior_group.draw(screen)
    red_warrior_group.update()

    blue_warrior_group.draw(screen)
    blue_warrior_group.update()

    red_hit_bullets = pygame.sprite.spritecollide(blue_warrior_group.sprite, red_bullets_group, False)
    blue_hit_bullets = pygame.sprite.spritecollide(red_warrior_group.sprite, blue_bullets_group, False)

    if red_hit_bullets:
        kill_bullet_and_spawn_explosion()
        blue_warrior_group.sprite.do_damage()

    if blue_hit_bullets:
        kill_bullet_and_spawn_explosion()
        red_warrior_group.sprite.do_damage()

    if explosions:
        update_explosions()

    pygame.display.update()
    clock.tick(60)
