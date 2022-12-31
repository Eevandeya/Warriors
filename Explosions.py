from Inner import *
from Sounds import hit_sound, explosion_sound
import Images

class BulletExplosion:
    def __init__(self, x, y):
        self.x = x - 6
        self.y = y - 3
        self.lifetime = 0

    def update(self):
        if self.lifetime == 14:
            return True
        else:
            Images.screen.blit(Images.bullet_explosion_images[self.lifetime // 3], (self.x, self.y))
            self.lifetime += 1
            return False

class PlayerExplosion:
    def __init__(self, x, y):
        self.x = x - 15
        self.y = y - 15
        self.lifetime = 0

    def update(self):
        if self.lifetime == 18 - 1:
            return True
        else:
            Images.screen.blit(Images.player_explosion_images[self.lifetime // 3], (self.x, self.y))
            self.lifetime += 1
            return False

def kill_bullet_and_spawn_explosion():
    for bullet in red_hit_bullets + blue_hit_bullets:
        explosions.append(BulletExplosion(bullet.rect.x, bullet.rect.y))
        hit_sound.play()
        bullet.kill()


def update_explosions():
    for explosion in explosions:
        isdead = explosion.update()
        if isdead:
            explosions.remove(explosion)


def spawn_player_explosion(x, y):
    explosions.append(PlayerExplosion(x, y))
    explosion_sound.play()