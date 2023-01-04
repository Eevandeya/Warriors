import pygame
from random import choice
from Animations import LaserMelting

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


class LaserGun:
    def __init__(self,  warrior, visual):
        self.warrior = warrior
        self.visual = visual
        self.laser_frames = visual.laser_animation
        self.max_length = 10
        self.length = 0
        self.active = False

    def activate(self, enemy_left, enemy_right, enemy_front):
        self.active = True

        if self.warrior.game_side == 'bottom':

            if self.warrior.rect.top - enemy_front <= 180 \
                    and (self.warrior.rect.left + 12) < enemy_right \
                    and (self.warrior.rect.right - 12) > enemy_left:

                        y = self.warrior.rect.top - 20
                        x = self.warrior.rect.left + 13
                        dist = self.warrior.rect.top - enemy_front
                        self.length = dist // 20
                        i = self.length

                        while i != 0:
                            self.visual.screen.blit(choice(self.laser_frames), (x, y))
                            y -= 20
                            i -= 1

                        self.visual.screen.blit(choice(self.laser_frames), (x, enemy_front))

                        self.visual.screen.blit(self.visual.laser_on_player, (x - 5, enemy_front))

            else:
                self.length = self.max_length
                y = self.warrior.rect.top
                x = self.warrior.rect.left + 13
                n = self.max_length
                while n != 0:
                    self.visual.screen.blit(choice(self.laser_frames), (x, y))
                    y -= 20
                    n -= 1

                self.visual.screen.blit(self.visual.laser_explosion, (x - 5, y + 10))

    def melt_laser(self, animations_list, visual):
        if self.active:
            print('here')
            self.active = False
            animations_list.append(LaserMelting(self.warrior.rect.left + 13, self.warrior.rect.top, self.length))
