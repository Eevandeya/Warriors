import pygame

class GunBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_pos, side, screen):
        warrior_x, warrior_y = warrior_pos
        super().__init__()
        speed = 8
        self.side = side

        if side == 'bottom':
            self.image = screen.red_bullet
            self.speed = -speed
            self.border = 30
        else:
            self.image = screen.blue_bullet
            self.speed = speed
            self.border = 512 + 30

        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def update(self):
        self.rect.y += self.speed
        self.destroy()

    def destroy(self):
        if self.side == 'bottom':
            if self.rect.y < self.border:
                self.kill()
        else:
            if self.rect.y > self.border:
                self.kill()
