import Constants
import pygame
from Screen import display_character_frames

class PickingPanel:
    def __init__(self, side):
        if side == 'top':
            self.control_buttons = {'left': pygame.K_a, 'right': pygame.K_d}

        elif side == 'bottom':
            self.control_buttons = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}
        else:
            print('Неверный параметр side при создании объекта класса PickingPanel. (top/bottom)')
            exit()

        self.movement_delay = 10
        self.movement_delay_level = 0
        self.side = side
        self.pointer = 0

    def control(self):
        if not self.movement_delay_level:
            keys = pygame.key.get_pressed()

            if keys[self.control_buttons['right']] and self.pointer < 4:
                self.pointer += 1
            if keys[self.control_buttons['left']] and self.pointer > 0:
                self.pointer -= 1

            self.movement_delay_level = self.movement_delay

    def update(self):
        if self.side == 'top':
            display_character_frames(Constants.TOP_PICK_LINE, self.pointer)
        else:
            display_character_frames(Constants.BOTTOM_PICK_LINE, self.pointer)

        self.control()

        if self.movement_delay_level:
            self.movement_delay_level -= 1