class Animation:
    def __init__(self, x, y):
        self.lifetime = 0
        self.x = x
        self.y = y


class BulletExplosion(Animation):
    def __init__(self, x, y):
        super().__init__(x - 6, y - 3)


    def update(self, screen):
        if self.lifetime == 14:
            return True
        else:
            screen.display_bullet_explosion(self.lifetime, self.x, self.y)
            self.lifetime += 1
            return False


class PlayerExplosion(Animation):
    def __init__(self, x, y):
        super().__init__(x - 15, y - 15)

    def update(self, screen):
        if self.lifetime == 25 - 1:
            return True
        else:
            screen.display_player_explosion(self.lifetime, self.x, self.y)
            self.lifetime += 1
            return False
