from Screen import display_bullet_explosion, display_player_explosion

class BulletExplosion:
    def __init__(self, x, y):
        self.x = x - 6
        self.y = y - 3
        self.lifetime = 0

    def update(self):
        if self.lifetime == 14:
            return True
        else:
            display_bullet_explosion(self.lifetime, self.x, self.y)
            self.lifetime += 1
            return False

class PlayerExplosion:
    def __init__(self, x, y):
        self.x = x - 15
        self.y = y - 15
        self.lifetime = 0

    def update(self):
        if self.lifetime == 25 - 1:
            return True
        else:
            display_player_explosion(self.lifetime, self.x, self.y)
            self.lifetime += 1
            return False
