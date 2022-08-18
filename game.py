import pygame


class BottomWarriror(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/red_warrior.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 250))

        self.reload = 0

    def warrior_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.top > 201:
            self.rect.y -= 2
        if keys[pygame.K_DOWN] and self.rect.bottom < 392 - 9:
            self.rect.y += 2
        if keys[pygame.K_LEFT] and self.rect.left > 9:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT] and self.rect.right < 512 - 9:
            self.rect.x += 2

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

    def destroy(self):
        if self.rect.y <= -30:
            self.kill()

class TopWarriror(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/blue_warrior.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 100))

        self.reload = 0

    def warrior_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.top > 9:
            self.rect.y -= 2
        if keys[pygame.K_s] and self.rect.bottom < 201 - 9:
            self.rect.y += 2
        if keys[pygame.K_a] and self.rect.left > 9:
            self.rect.x -= 2
        if keys[pygame.K_d] and self.rect.right < 512 - 9:
            self.rect.x += 2

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

pygame.init()

width = 512
height = 392
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
battlefield = pygame.image.load('images/battlefield2.png').convert_alpha()

screen.fill('#FFFFFF')

w1 = pygame.sprite.GroupSingle()
w1.add(BottomWarriror())

w2 = pygame.sprite.GroupSingle()
w2.add(TopWarriror())

red_bullets_group = pygame.sprite.Group()
blue_bullets_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('#FFFFFF')

    screen.blit(battlefield, (0, 0))

    red_bullets_group.draw(screen)
    red_bullets_group.update()

    blue_bullets_group.draw(screen)
    blue_bullets_group.update()

    w1.draw(screen)
    w1.update()

    w2.draw(screen)
    w2.update()

    pygame.display.update()
    clock.tick(60)
