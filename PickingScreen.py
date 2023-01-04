import Constants
import pygame
import Sounds
from Warrior import Gunslinger, Laser


class PickingPanel:
    def __init__(self, side, screen):
        if side == 'top':
            self.control_buttons = {'left': pygame.K_a, 'right': pygame.K_d, 'pick': pygame.K_g}

        elif side == 'bottom':
            self.control_buttons = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'pick': pygame.K_RCTRL}
        else:
            print('Неверный параметр side при создании объекта класса PickingPanel. (top/bottom)')
            exit()

        self.movement_delay = 8
        self.movement_delay_level = 0
        self.side = side
        self.pointer = 0
        self.picked = False
        self.phrase_timer = 20
        self.sound_played = False
        self.switch_sound = Sounds.switch_sound
        self.pick_sound = Sounds.pick_sound

        self.screen = screen

    def control(self):
        if not self.movement_delay_level:
            keys = pygame.key.get_pressed()
            if not self.picked:

                if keys[self.control_buttons['right']] and self.pointer < 4:
                    self.pointer += 1
                    self.switch_sound.play()
                    self.movement_delay_level = self.movement_delay

                if keys[self.control_buttons['left']] and self.pointer > 0:
                    self.pointer -= 1
                    self.switch_sound.play()
                    self.movement_delay_level = self.movement_delay

                if keys[self.control_buttons['pick']]:
                    self.picked = True
                    self.pick_sound.play()

            else:
                if self.phrase_timer:
                    self.phrase_timer -= 1
                elif not self.sound_played:
                    self.sound_played = True

    def update(self):
        if self.side == 'top':
            self.screen.display_character_frames(Constants.TOP_PICK_LINE, self.pointer)
            self.screen.display_picking_character_name(self.pointer, Constants.TOP_NICKNAME_LINE, self.picked)
        else:
            self.screen.display_character_frames(Constants.BOTTOM_PICK_LINE, self.pointer)
            self.screen.display_picking_character_name(self.pointer, Constants.BOTTOM_NICKNAME_LINE, self.picked)

        self.control()

        if self.movement_delay_level:
            self.movement_delay_level -= 1


class PickingScreen:
    def __init__(self, game):
        self.top_panel = PickingPanel('top', game.screen)
        self.bottom_panel = PickingPanel('bottom', game.screen)
        self.game = game
        self.countdown = False
        self.start_timer = 100

    def update(self):
        self.game.screen.screen.blit(self.game.screen.choosing_field, (0, 0))
        self.bottom_panel.update()
        self.top_panel.update()

        if self.top_panel.picked and self.bottom_panel.picked and not self.countdown:
            self.countdown = True
            # Создание группы синего игрока
            self.game.battle.red_warrior_group.add(Laser('bottom', self.bottom_panel.pointer, self.game.screen))
            self.game.battle.blue_warrior_group.add(Gunslinger('top', self.top_panel.pointer, self.game.screen))

        if self.countdown:
            self.start_timer -= 1

        if not self.start_timer:
            self.game.game_stage = 'battle'
