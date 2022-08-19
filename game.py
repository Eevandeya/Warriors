import pygame


class BottomWarrior(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/red_warrior.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 400))

    reload = 0
    borders = {'top': 351, 'bottom': 533, 'right': 512 - 9, 'left': 9}
    speed = 2

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

        if keys[pygame.K_RCTRL] and not self.reload:
            red_bullets_group.add(RedBullet(self.rect.x, self.rect.y))
            self.reload = 10

    def update(self):
        self.warrior_control()

        if self.reload:
            self.reload -= 1


class RedBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_x, warrior_y):
        super().__init__()
        self.image = pygame.image.load('images/red_bullet.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def update(self):
        self.rect.y -= 4
        self.destroy()

    def destroy(self):
        if self.rect.y <= -30:
            self.kill()


class TopWarrior(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/blue_warrior.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 250))

    reload = 0
    borders = {'top': 159, 'bottom': 341, 'right': 512 - 9, 'left': 9}
    speed = 2

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

        if keys[pygame.K_g] and not self.reload:
            blue_bullets_group.add(BlueBullet(self.rect.x, self.rect.y))
            self.reload = 10

    def update(self):
        self.warrior_control()

        if self.reload:
            self.reload -= 1


class BlueBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_x, warrior_y):
        super().__init__()
        self.image = pygame.image.load('images/blue_bullet.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def update(self):
        self.rect.y += 4

    def destroy(self):
        if self.rect.y > 512 + 30:
            self.kill()


class Explosion:
    def __init__(self, x, y):
        self.x = x - 6
        self.y = y - 3
        self.lifetime = 10

    def update(self):
        if self.lifetime == 0:
            return True
        else:
            self.lifetime -= 1
            screen.blit(explosion_image, (self.x, self.y))
            return False


def kill_bullet_and_spawn_explosion():
    for bullet in hit_bullets:
        explosions.append(Explosion(bullet.rect.x, bullet.rect.y))
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
explosion_image = pygame.image.load('images/explosion3.png').convert_alpha()
full_heart = pygame.image.load('images/full_heart.png').convert_alpha()
full_bullet = pygame.image.load('images/full_bullet_2.png')

# a = 48
# full_bullet = pygame.transform.scale(full_bullet, (a, a))
# full_haerd = pygame.transform.scale(full_haerd, (a, a))


screen.fill('#FFFFFF')


w1 = pygame.sprite.GroupSingle()
w1.add(BottomWarrior())

w2 = pygame.sprite.GroupSingle()
w2.add(TopWarrior())

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


    gap_between_hearts = 64
    gap_between_bullets = 42

    heart_indent = 20
    bullet_indent = 270

    top_line = 43
    bottom_line = 585


    for i in range(5):
        screen.blit(full_bullet, (i*gap_between_bullets + bullet_indent, top_line))

    for i in range(3):
        screen.blit(full_heart, (i*gap_between_hearts + heart_indent, top_line))

    for i in range(5):
        screen.blit(full_bullet, (i*gap_between_bullets + bullet_indent, bottom_line))

    for i in range(3):
        screen.blit(full_heart, (i*gap_between_hearts + heart_indent, bottom_line))

    red_bullets_group.draw(screen)
    red_bullets_group.update()

    blue_bullets_group.draw(screen)
    blue_bullets_group.update()

    w1.draw(screen)
    w1.update()

    w2.draw(screen)
    w2.update()

    hit_bullets = pygame.sprite.spritecollide(w2.sprite, red_bullets_group, False) + \
                  pygame.sprite.spritecollide(w1.sprite, blue_bullets_group, False)

    if hit_bullets:
        kill_bullet_and_spawn_explosion()

    if explosions:
        update_explosions()

    pygame.display.update()
    clock.tick(60)
