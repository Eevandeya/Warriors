import pygame

class Warrior1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('warrior_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(400, 200))

    def warrior_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1

    def update(self):
        self.warrior_move()

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('#FFFFFF')
    w1.draw(screen)
    w1.update()

    pygame.display.update()
    clock.tick(60)
