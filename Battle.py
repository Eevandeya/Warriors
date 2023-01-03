import pygame
import Sounds
from Bullet import GunBullet
import Constants
import Animations

class Battle:
    def __init__(self, game):
        self.game = game
        self.red_bullets_group = pygame.sprite.Group()
        self.blue_bullets_group = pygame.sprite.Group()
        self.winner = None
        self.end_screen_delay = Constants.ENDSCREEN_DELAY
        self.play_win_sound = True
        self.explosions = []

        self.red_warrior_group = pygame.sprite.GroupSingle()
        self.blue_warrior_group = pygame.sprite.GroupSingle()


    def update_explosions(self):
        for explosion in self.explosions:
            isdead = explosion.update(self.game.screen)
            if isdead:
                self.explosions.remove(explosion)


    def spawn_player_explosion(self, x, y):
        self.explosions.append(Animations.PlayerExplosion(x, y))
        if not self.blue_warrior_group.sprite.isAlive:
            self.blue_warrior_group.sprite.death_sound.play()
        else:
            self.red_warrior_group.sprite.death_sound.play()


    def kill_bullet_and_spawn_explosions(self, bhb, rhb):
        red_dead = False
        blue_dead = False

        for bullet in bhb:
            if self.red_warrior_group.sprite.heals == 0:
                self.explosions.append(Animations.PlayerExplosion(self.red_warrior_group.sprite.rect.centerx,
                                                                  self.red_warrior_group.sprite.rect.centery))
                self.red_warrior_group.sprite.death_sound.play()
                red_dead = True

            else:
                self.explosions.append(Animations.BulletExplosion(bullet.rect.x, bullet.rect.y))
                self.red_warrior_group.sprite.hit_sound.play()

            bullet.kill()

        for bullet in rhb:
            if self.blue_warrior_group.sprite.heals == 0:
                self.explosions.append(Animations.PlayerExplosion(self.blue_warrior_group.sprite.rect.centerx,
                                                                  self.blue_warrior_group.sprite.rect.centery))
                self.blue_warrior_group.sprite.death_sound.play()
                blue_dead = True

            else:
                self.explosions.append(Animations.BulletExplosion(bullet.rect.x, bullet.rect.y))
                self.blue_warrior_group.sprite.hit_sound.play()

            bullet.kill()

        return red_dead, blue_dead


    def update(self):
        self.game.screen.screen.fill('#dcdcdc')
        self.game.screen.screen.blit(self.game.screen.battlefield, (0, 150))

        self.red_bullets_group.draw(self.game.screen.screen)
        self.blue_bullets_group.draw(self.game.screen.screen)
        self.red_bullets_group.update()
        self.blue_bullets_group.update()

        # Обновление игроков
        self.red_warrior_group.update(self.game.screen)
        self.blue_warrior_group.update(self.game.screen)

        # Получение списков пуль, которые попали
        red_hit_bullets = pygame.sprite.spritecollide(self.blue_warrior_group.sprite, self.red_bullets_group, False)
        blue_hit_bullets = pygame.sprite.spritecollide(self.red_warrior_group.sprite, self.blue_bullets_group, False)

        if self.game.game_stage == 'battle':

            # Обработка выстрелов, если они есть
            blue_shot = self.blue_warrior_group.sprite.warrior_shots()
            red_shot = self.red_warrior_group.sprite.warrior_shots()

            if blue_shot != False:
                self.blue_bullets_group.add(GunBullet(blue_shot, 'top', self.game.screen))
            if red_shot != False:
                self.red_bullets_group.add(GunBullet(red_shot, 'bottom', self.game.screen))

            # Если какие-то пули попали, уничтожение их, спавн взрывов
            # и начисление повреждений игрокам
            isRedDead, isBlueDead = False, False

            if red_hit_bullets or blue_hit_bullets:

                if red_hit_bullets:
                    self.blue_warrior_group.sprite.do_damage(len(red_hit_bullets))

                if blue_hit_bullets:
                    self.red_warrior_group.sprite.do_damage(len(blue_hit_bullets))

                isRedDead, isBlueDead = self.kill_bullet_and_spawn_explosions(blue_hit_bullets, red_hit_bullets)

            # Отрисовка игроков
            self.red_warrior_group.draw(self.game.screen.screen)
            self.blue_warrior_group.draw(self.game.screen.screen)

            # Обработка смертей игроков
            if isBlueDead:
                self.game.game_stage = 'end'
                self.winner = 'red'
                self.blue_warrior_group.sprite.isAlive = False

            if isRedDead:
                self.game.game_stage = 'end'
                self.winner = 'blue'
                self.red_warrior_group.sprite.isAlive = False

        elif self.game.game_stage == 'end':

            # В двух ветвях происходит отрисовка победителя, обработка пуль противников, определение эндскрина
            # Обработка выстрелов победителя
            if self.winner == 'red':
                self.red_warrior_group.draw(self.game.screen.screen)
                if blue_hit_bullets:
                    self.kill_bullet_and_spawn_explosions(blue_hit_bullets, red_hit_bullets)

                end_screen = self.game.screen.red_wins
                red_shot = self.red_warrior_group.sprite.warrior_shots()

                if red_shot != False:
                    self.red_bullets_group.add(GunBullet(red_shot, 'bottom', self.game.screen))

            else:
                self.blue_warrior_group.draw(self.game.screen.screen)
                if red_hit_bullets:
                    self.kill_bullet_and_spawn_explosions(red_hit_bullets, blue_hit_bullets)

                end_screen = self.game.screen.blue_wins

                blue_shot = self.blue_warrior_group.sprite.warrior_shots()
                if blue_shot != False:
                    self.blue_bullets_group.add(GunBullet(blue_shot, 'top', self.game.screen))

            # После победы, нужно выждать задержку, после появляется эндскрин, играется звук
            if not self.end_screen_delay:

                if self.play_win_sound:
                    Sounds.win_sound.play()
                self.play_win_sound = False

                self.game.screen.screen.blit(end_screen, (0, 0))

            else:
                self.end_screen_delay -= 1

        if self.explosions:
            self.update_explosions()
