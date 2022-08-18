import pygame

class Warrior1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('warrior_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(400, 200))

        self.reload = 0

    def warrior_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2

        if keys[pygame.K_SPACE] and not(self.reload):
            bullets_group.add(Bullet(self.rect.x, self.rect.y))
            self.reload = 10

    def update(self):
        self.warrior_control()

        if self.reload:
            self.reload -= 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, warrior_x, warrior_y):
        super().__init__()
        self.image = pygame.image.load('bullet_2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))


    def update(self):
        self.rect.y -= 4

    def destroy(self):
        if self.rect.y <= -30:
            self.kill()


pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()


screen.fill('#FFFFFF')

# warrior_surf = pygame.image.load('warrior_1.png').convert_alpha()
# warrior_rect = warrior_surf.get_rect(topleft=(400, 200))

w1 = pygame.sprite.GroupSingle()
w1.add(Warrior1())

bullets_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('#FFFFFF')

    bullets_group.draw(screen)
    bullets_group.update()

    w1.draw(screen)
    w1.update()

    pygame.display.update()
    clock.tick(60)
