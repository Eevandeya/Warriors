import pygame
import Sounds
from Arsenal import GunBullet
import Constants
import Animations


class Battle:
    def __init__(self, game):
        self.game = game
        self.end_screen_delay = Constants.ENDSCREEN_DELAY
        self.play_win_sound = True
        self.animations = []

        self.red_warrior_group = pygame.sprite.GroupSingle()
        self.blue_warrior_group = pygame.sprite.GroupSingle()

    def update_animations(self):
        for animation in self.animations:
            isdead = animation.display(self.game.visual)
            if isdead:
                self.animations.remove(animation)

    def update(self):
        self.game.visual.screen.fill('#dcdcdc')
        self.game.visual.screen.blit(self.game.visual.battlefield, (0, 150))

        # Обновление игроков
        self.red_warrior_group.update(self.blue_warrior_group.sprite, self.animations)
        self.blue_warrior_group.update(self.red_warrior_group.sprite, self.animations)

        if self.game.game_stage == 'battle':

            self.red_warrior_group.draw(self.game.visual.screen)
            self.blue_warrior_group.draw(self.game.visual.screen)

            # Обработка смертей игроков
            if not self.blue_warrior_group.sprite.isAlive:
                self.game.game_stage = 'end'
                self.winner = 'red'

            if not self.red_warrior_group.sprite.isAlive:
                self.game.game_stage = 'end'
                self.winner = 'blue'

        elif self.game.game_stage == 'end':

            # В двух ветвях происходит отрисовка победителя, обработка пуль противников, определение эндскрина
            # Обработка выстрелов победителя
            if self.winner == 'red':
                self.red_warrior_group.draw(self.game.visual.screen)
                end_screen = self.game.visual.red_wins

            else:
                self.blue_warrior_group.draw(self.game.visual.screen)
                end_screen = self.game.visual.blue_wins

            # После победы, нужно выждать задержку, после появляется эндскрин, играется звук
            if not self.end_screen_delay:

                if self.play_win_sound:
                    Sounds.win_sound.play()
                self.play_win_sound = False

                self.game.visual.screen.blit(end_screen, (0, 0))

            else:
                self.end_screen_delay -= 1

        # print(self.animations)
        if self.animations:
            self.update_animations()
