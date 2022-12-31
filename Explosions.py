import pygame
from Screen import display_bullet_explosion

class BulletExplosion:
    def __init__(self, x, y):
        self.x = x - 6
        self.y = y - 3
        self.lifetime = 0

    def update(self):
        if self.lifetime == 14:
            return True
        else:
            display_bullet_explosion(self.lifetime, self.x, self.y)
            self.lifetime += 1
            return False

class PlayerExplosion:
    def __init__(self, x, y):
        self.x = x - 15
        self.y = y - 15
        self.lifetime = 0

    def update(self):
        if self.lifetime == 18 - 1:
            return True
        else:
            display_bullet_explosion(self.lifetime, self.x, self.y)
            self.lifetime += 1
            return False
