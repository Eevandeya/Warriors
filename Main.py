from PickingScreen import *
from Battle import *
from Visual import *


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.visual = Visual()
        self.game_stage = 'pick'
        self.picking_screen = PickingScreen(self)
        self.battle = Battle(self)

    def new_game(self):
        self.game_stage = 'pick'
        self.picking_screen = PickingScreen(self)
        self.battle = Battle(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_stage == 'end':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.new_game()

    def run(self):
        while True:
            self.check_events()

            if self.game_stage == 'pick':
                self.picking_screen.update()
            else:
                self.battle.update()

            pygame.display.update()
            self.clock.tick(Constants.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
