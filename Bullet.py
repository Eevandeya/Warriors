import pygame
import Images

class RedBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_x, warrior_y):
        super().__init__()
        self.image = Images.red_bullet
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def update(self):
        self.rect.y -= 6
        self.destroy()

    def destroy(self):
        if self.rect.y <= -30:
            self.kill()


class BlueBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_x, warrior_y):
        super().__init__()
        self.image = Images.blue_bullet
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def update(self):
        self.rect.y += 6

    def destroy(self):
        if self.rect.y > 512 + 30:
            self.kill()
