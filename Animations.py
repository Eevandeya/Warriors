from random import choice


class Animation:
    def __init__(self, x, y):
        self.lifetime = 0
        self.x = x
        self.y = y


class BulletExplosion(Animation):
    def __init__(self, x, y):
        super().__init__(x - 6, y - 3)

    def display(self, visual):
        if self.lifetime == 14:
            return True
        else:
            visual.screen.blit(visual.bullet_explosion_images[self.lifetime // 3], (self.x - 5, self.y - 5))
            self.lifetime += 1
            return False


class PlayerExplosion(Animation):
    def __init__(self, x, y):
        super().__init__(x - 15, y - 15)

    def display(self, visual):
        if self.lifetime == 25 - 1:
            return True
        else:
            visual.screen.blit(visual.player_explosion_images[self.lifetime // 5], (self.x - 16, self.y - 16))
            self.lifetime += 1
            return False


class LaserMelting(Animation):
    def __init__(self, x, y, length, enemy_front):
        super().__init__(x, y)
        self.length = length
        self.time = 5
        self.enemy_front = enemy_front

    def display(self, visual):
        if self.lifetime <= self.time:
            frames = visual.laser_melting_stage_1
        elif self.lifetime <= self.time*2:
            frames = visual.laser_melting_stage_2
        elif self.lifetime <= self.time*3:
            frames = visual.laser_melting_stage_3
        else:
            return True


        for i in range(self.length):
            visual.screen.blit(choice(frames), (self.x, self.y - i * 20))

        if self.enemy_front:
            visual.screen.blit(choice(frames), (self.x, self.enemy_front))

        self.lifetime += 1

        return False
