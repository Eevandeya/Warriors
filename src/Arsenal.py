import pygame
from random import choice, randint

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
        self.laser_explosion_frames = visual.laser_explosion_animation
        self.max_length = 10
        self.length = 0
        self.active = False
        self.damaging = False

        self.sound_playing = False
        self.sound_delay = Constants.FPS * 6 + 8
        self.sound_delay_level = 0
        self.damage_sound_delay = Constants.FPS * 2 - 20
        self.damage_sound_delay_level = 0

        self.animation_stage = 0
        self.animation_speed = 3

    def play_explosion_animation(self, x, y):
        if self.animation_stage <= self.animation_speed:
            self.visual.screen.blit(self.laser_explosion_frames[0], (x, y))
        elif self.animation_stage <= self.animation_speed*2:
            self.visual.screen.blit(self.laser_explosion_frames[1], (x, y))
        elif self.animation_stage <= self.animation_speed*3:
            self.visual.screen.blit(self.laser_explosion_frames[2], (x, y))
        elif self.animation_stage <= self.animation_speed*4:
            self.visual.screen.blit(self.laser_explosion_frames[3], (x, y))
        elif self.animation_stage <= self.animation_speed*5:
            self.visual.screen.blit(self.laser_explosion_frames[4], (x, y))
        elif self.animation_stage <= self.animation_speed*6:
            self.visual.screen.blit(self.laser_explosion_frames[5], (x, y))
        else:
            self.animation_stage = 0
            self.visual.screen.blit(self.laser_explosion_frames[0], (x, y))

        self.animation_stage += 1

    def play_active_sound(self):
        if not self.sound_delay_level:
            self.warrior.laser_sound.play()
            self.sound_delay_level = self.sound_delay

        else:
            self.sound_delay_level -= 1

    def play_damage_sound(self):
        if self.damaging and not self.damage_sound_delay_level:
            self.warrior.laser_damage_sound.play()
            self.damage_sound_delay_level = self.damage_sound_delay
        if not self.damaging:
            self.damage_sound_delay_level = 0
            self.warrior.laser_damage_sound.stop()
        else:
            self.damage_sound_delay_level -= 1

    def stop_playing_sounds(self):
        self.sound_delay_level = 0
        self.damage_sound_delay_level = 0
        self.warrior.laser_sound.stop()
        self.warrior.laser_damage_sound.stop()

    def activate(self, enemy_left, enemy_right, enemy_front):
        self.active = True
        self.play_active_sound()
        self.play_damage_sound()

        if self.warrior.is_top_side:
            y = self.warrior.rect.bottom
            x = self.warrior.rect.left + 12

            if enemy_front - self.warrior.rect.bottom <= 20 * self.max_length \
                    and (self.warrior.rect.left + 12) < enemy_right \
                    and (self.warrior.rect.right - 12) > enemy_left:

                self.damaging = True
                dist = enemy_front - self.warrior.rect.bottom
                self.length = dist // 20
                self.last_enemy_front = enemy_front

            else:
                self.damaging = False
                self.length = self.max_length

            for i in range(self.length):
                self.visual.screen.blit(choice(self.laser_frames), (x, y + i * 20))

            if self.damaging:
                self.visual.screen.blit(choice(self.laser_frames), (x, enemy_front - 20))
                # self.visual.screen.blit(self.visual.laser_on_player, (x - 4, enemy_front))
            else:
                self.play_explosion_animation(x - 12, y + self.max_length * 20 - 10)

            return self.damaging

        else:

            y = self.warrior.rect.top - 20
            x = self.warrior.rect.left + 12

            if self.warrior.rect.top - enemy_front <= 20 * self.max_length \
                    and (self.warrior.rect.left + 12) < enemy_right \
                    and (self.warrior.rect.right - 12) > enemy_left:

                self.damaging = True
                dist = self.warrior.rect.top - enemy_front
                self.length = dist // 20
                self.last_enemy_front = enemy_front

            else:
                self.damaging = False
                self.length = self.max_length

            for i in range(self.length):
                self.visual.screen.blit(choice(self.laser_frames), (x, y - i * 20))

            if self.damaging:
                self.visual.screen.blit(choice(self.laser_frames), (x, enemy_front))
                self.visual.screen.blit(self.visual.laser_on_player, (x - 4, enemy_front))
            else:
                self.play_explosion_animation(x - 12, y - self.max_length * 20 + 10)

            return self.damaging

    def melt_laser(self, animations_list):
        if self.active:
            self.active = False
            self.stop_playing_sounds()

            if self.length == self.max_length or self.last_enemy_front == (self.warrior.rect.y - (self.length - 1) * 20):
                enemy_front = 0
            else:
                enemy_front = self.last_enemy_front

            if self.warrior.is_top_side:
                y = self.warrior.rect.bottom
            else:
                y = self.warrior.rect.top - 20

            animations_list.append(LaserMelting(self.warrior.rect.left + 12,
                                                y,
                                                self.length,
                                                enemy_front,
                                                self.warrior.is_top_side))


class Sting(pygame.sprite.Sprite):
    def __init__(self, warrior_pos, is_top_side, is_left_launching, visual):
        super().__init__()
        warrior_x, warrior_y = warrior_pos
        self.is_launching = True
        self.y_speed = 0
        self.is_top_side = is_top_side
        self.correction = 0.1

        if is_left_launching:
            self.x_speed = 5
            start_x = warrior_x + 24
        else:
            self.x_speed = -5
            start_x = warrior_x

        if is_top_side:
            self.border = 512 + 30
            self.y_speed_acceleration = 0.7  # *10 == self.y_speed
            self.image = visual.blue_sting
        else:
            self.border = 30
            self.y_speed_acceleration = -0.7  # *10 == self.y_speed
            self.image = visual.red_sting

        self.rect = self.image.get_rect(topleft=(start_x, warrior_y + 8))

        self.is_left_launched = is_left_launching

    def launching(self):
        if self.is_left_launched:
            self.x_speed -= 0.5
        else:
            self.x_speed += 0.5

        self.y_speed += self.y_speed_acceleration

        if not self.x_speed:
            self.is_launching = False

    def aiming(self, enemy_centerx, enemy_bottom):
        if self.is_top_side:
            if enemy_bottom < self.rect.top:
                return
        else:
            if enemy_bottom > self.rect.bottom:
                return

        diff = enemy_centerx - self.rect.centerx
        if diff == 0:
            pass
        elif diff > 0:
            self.x_speed += self.correction
        else:
            self.x_speed -= self.correction

    def hit(self, animations):
        Sounds.sting_hit.play()
        animations.append(BulletExplosion(self.rect.x, self.rect.y))
        self.kill()

    def update(self, enemy_centerx, enemy_bottom):
        if self.is_launching:
            self.launching()
        else:
            self.aiming(enemy_centerx, enemy_bottom)

        self.rect.y += int(self.y_speed)
        self.rect.x += int(self.x_speed)

        self.destroy()

    def destroy(self):
        if not self.is_top_side:
            if self.rect.y < self.border:
                self.kill()
        else:
            if self.rect.y > self.border:
                self.kill()


class Pellet(pygame.sprite.Sprite):
    def __init__(self, warrior_pos, is_top_side, visual, speed):
        warrior_x, warrior_y = warrior_pos
        super().__init__()
        self.is_top_side = is_top_side
        spread = 100
        self.x_speed = randint(-spread, spread) / 100
        self.x_pos = warrior_x + 13

        if is_top_side:
            self.image = visual.blue_pellet
            self.speed = speed
            self.border = 512 + 30

        else:
            self.image = visual.red_pellet
            self.speed = -speed
            self.border = 30

        self.rect = self.image.get_rect(topleft=(warrior_x + 13, warrior_y))

    def update(self):
        self.rect.y += self.speed

        self.x_pos += self.x_speed
        self.rect.x = int(self.x_pos)
        self.destroy()

    def hit(self, animations):
        Sounds.pellet_hit.play()
        animations.append(BulletExplosion(self.rect.x, self.rect.y))
        self.kill()

    def destroy(self):
        if not self.is_top_side:
            if self.rect.y < self.border:
                self.kill()
        else:
            if self.rect.y > self.border:
                self.kill()
