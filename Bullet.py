import pygame
import Screen

class RedBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_pos):
        warrior_x, warrior_y = warrior_pos
        super().__init__()
        self.image = Screen.red_bullet
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.y <= -30:
            self.kill()


class BlueBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_pos):
        warrior_x, warrior_y = warrior_pos
        super().__init__()
        self.image = Screen.blue_bullet
        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))
        self.speed = 9

    def update(self):
        self.rect.y += self.speed

    def destroy(self):
        if self.rect.y > 512 + 30:
            self.kill()
