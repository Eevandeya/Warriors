import Constants
import pygame
import Sounds
from Warrior import Gunslinger, Laser


class PickingPanel:
    def __init__(self, side, visual):
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

        self.visual = visual

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

    def display_picking_character_name(self, line):
        if self.picked:
            self.visual.screen.blit(self.visual.chosen_nickname_frame, (Constants.NICKNAME_FRAME_INDENT, line))
            if self.pointer == 1:
                self.visual.screen.blit(self.visual.green_family_nicknames[self.pointer],
                                        (Constants.NICKNAME_INDENT + 32, line + 22))
            else:
                self.visual.screen.blit(self.visual.green_family_nicknames[self.pointer],
                                        (Constants.NICKNAME_INDENT, line + 22))

        else:
            self.visual.screen.blit(self.visual.empty_nickname_frame, (Constants.NICKNAME_FRAME_INDENT, line))
            if self.pointer == 1:
                self.visual.screen.blit(self.visual.family_nicknames[self.pointer],
                                        (Constants.NICKNAME_INDENT + 32, line + 22))
            else:
                self.visual.screen.blit(self.visual.family_nicknames[self.pointer],
                                        (Constants.NICKNAME_INDENT, line + 22))

    def display_character_frames(self, line):
        for i in range(5):
            if i == self.pointer:
                self.visual.screen.blit(self.visual.chosen_frame,
                                        (i * Constants.GAP_BETWEEN_FRAMES + Constants.FRAME_INDENT, line))
            else:
                self.visual.screen.blit(self.visual.empty_frame,
                                        (i * Constants.GAP_BETWEEN_FRAMES + Constants.FRAME_INDENT, line))

            self.visual.screen.blit(self.visual.family[i],
                                    (i * Constants.GAP_BETWEEN_FRAMES + 46, line + 25))

    def update(self):
        if self.side == 'top':
            self.display_character_frames(Constants.TOP_PICK_LINE)
            self.display_picking_character_name(Constants.TOP_NICKNAME_LINE)
        else:
            self.display_character_frames(Constants.BOTTOM_PICK_LINE)
            self.display_picking_character_name(Constants.BOTTOM_NICKNAME_LINE)

        self.control()

        if self.movement_delay_level:
            self.movement_delay_level -= 1


class PickingScreen:
    def __init__(self, game):
        self.top_panel = PickingPanel('top', game.visual)
        self.bottom_panel = PickingPanel('bottom', game.visual)
        self.game = game
        self.countdown = False
        self.start_timer = 100

    def update(self):
        self.game.visual.screen.blit(self.game.visual.choosing_field, (0, 0))
        self.bottom_panel.update()
        self.top_panel.update()

        if self.top_panel.picked and self.bottom_panel.picked and not self.countdown:
            self.countdown = True
            # Создание группы синего игрока
            self.game.battle.red_warrior_group.add(Gunslinger('bottom', self.bottom_panel.pointer, self.game.visual))
            self.game.battle.blue_warrior_group.add(Gunslinger('top', self.top_panel.pointer, self.game.visual))

        if self.countdown:
            self.start_timer -= 1

        if not self.start_timer:
            self.game.game_stage = 'battle'
