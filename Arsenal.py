import pygame
from random import choice

import Constants
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
        self.damaging = False

        self.sound_playing = False
        self.sound_delay = Constants.FPS * 6 + 8
        self.sound_delay_level = 0
        self.damage_sound_delay = Constants.FPS * 2 - 20
        self.damage_sound_delay_level = 0

    def play_active_sound(self):
        if not self.sound_delay_level:
            Sounds.laser_sound.play()
            self.sound_delay_level = self.sound_delay

        else:
            self.sound_delay_level -= 1

    def play_damage_sound(self):
        if self.damaging and not self.damage_sound_delay_level:
            Sounds.laser_damage_sound.play()
            self.damage_sound_delay_level = self.damage_sound_delay
        if not self.damaging:
            self.damage_sound_delay_level = 0
            Sounds.laser_damage_sound.stop()
        else:
            self.damage_sound_delay_level -= 1

    def stop_playing_sounds(self):
        self.sound_delay_level = 0
        self.damage_sound_delay_level = 0
        Sounds.laser_sound.stop()
        Sounds.laser_damage_sound.stop()

    def activate(self, enemy_left, enemy_right, enemy_front):
        self.active = True
        self.play_active_sound()
        self.play_damage_sound()

        if self.warrior.is_top_side:
            sign = -1
            front = self.warrior.rect.bottom
            y = front
        else:
            front = self.warrior.rect.top
            sign = 1
            y = front - 20


        # if not self.warrior.is_top_side:
        x = self.warrior.rect.left + 12

        if sign*(front - enemy_front) <= 20*self.max_length \
                and (self.warrior.rect.left + 12) < enemy_right \
                and (self.warrior.rect.right - 12) > enemy_left:

            self.damaging = True
            dist = abs(front - enemy_front)
            self.length = dist // 20
            self.last_enemy_front = enemy_front

        else:
            self.damaging = False
            self.length = self.max_length

        for i in range(self.length):
            self.visual.screen.blit(choice(self.laser_frames), (x, y - sign*i*20))

        if self.damaging:
            if self.warrior.is_top_side:
                self.visual.screen.blit(choice(self.laser_frames), (x, enemy_front - 20))
            else:
                self.visual.screen.blit(choice(self.laser_frames), (x, enemy_front))

            self.visual.screen.blit(self.visual.laser_on_player, (x - 4, enemy_front))
        else:
            self.visual.screen.blit(self.visual.laser_explosion, (x - 4, y - sign*self.max_length * 20 + sign*10))

        return self.damaging


        # else:
        #     y = self.warrior.rect.bottom - 20
        #     x = self.warrior.rect.left + 12
        #
        #     if enemy_front - self.warrior.rect.top <= 20 * self.max_length \
        #             and (self.warrior.rect.left + 12) < enemy_right \
        #             and (self.warrior.rect.right - 12) > enemy_left:
        #
        #         self.damaging = True
        #         dist = enemy_front - self.warrior.rect.top
        #         self.length = dist // 20
        #         self.last_enemy_front = enemy_front
        #
        #     else:
        #         self.damaging = False
        #         self.length = self.max_length
        #
        #     for i in range(self.length):
        #         self.visual.screen.blit(choice(self.laser_frames), (x, y + i * 20))
        #
        #     if self.damaging:
        #         self.visual.screen.blit(choice(self.laser_frames), (x, enemy_front))
        #         self.visual.screen.blit(self.visual.laser_on_player, (x - 5, enemy_front))
        #     else:
        #         self.visual.screen.blit(self.visual.laser_explosion, (x - 5, y + self.max_length * 20 - 10))
        #
        #     return self.damaging


    def melt_laser(self, animations_list):
        if self.active:
            self.active = False
            self.stop_playing_sounds()

            if self.length == self.max_length or self.last_enemy_front == (self.warrior.rect.y - (self.length - 1) * 20):
                front = 0
            else:
                front = self.last_enemy_front

            animations_list.append(LaserMelting(self.warrior.rect.left + 12,
                                                self.warrior.rect.top - 20, self.length, front))
