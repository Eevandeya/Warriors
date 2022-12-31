import Constants
import pygame
from Sounds import switch_sound, pick_sound
from Screen import display_character_frames, display_picking_character_name

class PickingPanel:
    def __init__(self, side):
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

    def control(self):
        if not self.movement_delay_level:
            keys = pygame.key.get_pressed()
            if not self.picked:

                if keys[self.control_buttons['right']] and self.pointer < 4:
                    self.pointer += 1
                    switch_sound.play()
                    self.movement_delay_level = self.movement_delay

                if keys[self.control_buttons['left']] and self.pointer > 0:
                    self.pointer -= 1
                    switch_sound.play()
                    self.movement_delay_level = self.movement_delay

                if keys[self.control_buttons['pick']]:
                    self.picked = True
                    pick_sound.play()

    def update(self):
        if self.side == 'top':
            display_character_frames(Constants.TOP_PICK_LINE, self.pointer)
            display_picking_character_name(self.pointer, Constants.TOP_NICKNAME_LINE, self.picked)
        else:
            display_character_frames(Constants.BOTTOM_PICK_LINE, self.pointer)
            display_picking_character_name(self.pointer, Constants.BOTTOM_NICKNAME_LINE, self.picked)

        self.control()

        if self.movement_delay_level:
            self.movement_delay_level -= 1
