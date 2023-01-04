import pygame
from random import choice
import Sounds
from Animations import LaserMelting, BulletExplosion


class GunBullet(pygame.sprite.Sprite):
    def __init__(self, warrior_pos, is_top_side, visual, speed):
        warrior_x, warrior_y = warrior_pos
        super().__init__()
        self.is_top_side = is_top_side

        if not is_top_side:
            self.image = visual.red_bullet
            self.speed = -speed
            self.border = 30
        else:
            self.image = visual.blue_bullet
            self.speed = speed
            self.border = 512 + 30

        self.rect = self.image.get_rect(topleft=(warrior_x + 6, warrior_y))

    def hit(self, animations, is_not_one_hp):
        if is_not_one_hp:
            Sounds.hit_sound.play()
            animations.append(BulletExplosion(self.rect.x, self.rect.y))
        self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()

    def destroy(self):
        if not self.is_top_side:
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
        self.last_enemy_front = 0

    def activate(self, enemy_left, enemy_right, enemy_front):
        self.active = True

        if not self.warrior.is_top_side:

            if self.warrior.rect.top - enemy_front <= 20*self.max_length \
                    and (self.warrior.rect.left + 12) < enemy_right \
                    and (self.warrior.rect.right - 12) > enemy_left:

                y = self.warrior.rect.top - 20
                x = self.warrior.rect.left + 13
                dist = self.warrior.rect.top - enemy_front

                self.length = dist // 20
                self.last_enemy_front = enemy_front

                for i in range(self.length):
                    self.visual.screen.blit(choice(self.laser_frames), (x, y - i*20))

                self.visual.screen.blit(choice(self.laser_frames), (x, enemy_front))

                self.visual.screen.blit(self.visual.laser_on_player, (x - 5, enemy_front))

            else:
                self.length = self.max_length
                y = self.warrior.rect.top - 20
                x = self.warrior.rect.left + 12


                for i in range(self.max_length):
                    self.visual.screen.blit(choice(self.laser_frames), (x, y - i*20))

                self.visual.screen.blit(self.visual.laser_explosion, (x - 5, y - self.max_length * 20 + 10))

    def melt_laser(self, animations_list):
        if self.active:
            self.active = False

            if self.length == self.max_length or self.last_enemy_front == (self.warrior.rect.y - (self.length - 1) * 20):
                front = 0
            else:
                front = self.last_enemy_front

            animations_list.append(LaserMelting(self.warrior.rect.left + 12,
                                                self.warrior.rect.top - 20, self.length, front))
