import pygame
from Screen import screen, battlefield, red_wins_background, blue_wins_background
from Warrior import Warrior
import Constants
from Bullet import RedBullet, BlueBullet
import Sounds
import Explosions

def kill_bullet_and_spawn_explosion():
    for bullet in red_hit_bullets + blue_hit_bullets:
        explosions.append(Explosions.BulletExplosion(bullet.rect.x, bullet.rect.y))
        Sounds.hit_sound.play()
        bullet.kill()


def update_explosions():
    for explosion in explosions:
        isdead = explosion.update()
        if isdead:
            explosions.remove(explosion)


def spawn_player_explosion(x, y):
    explosions.append(Explosions.PlayerExplosion(x, y))
    Sounds.explosion_sound.play()


def reset_game():
    global game_stage, end_screen_delay, explosions, winner, play_win_sound

    red_warrior_group.empty()
    blue_warrior_group.empty()
    red_bullets_group.empty()
    blue_bullets_group.empty()

    red_warrior_group.add(Warrior('bottom'))
    blue_warrior_group.add(Warrior('top'))

    game_stage = 'battle'
    end_screen_delay = Constants.ENDSCREEN_DELAY
    explosions = []
    winner = None
    play_win_sound = True

pygame.init()

clock = pygame.time.Clock()

# Создание группы красного игрока
red_warrior_group = pygame.sprite.GroupSingle()
red_warrior_group.add(Warrior('bottom'))

# Создание группы синего игрока
blue_warrior_group = pygame.sprite.GroupSingle()
blue_warrior_group.add(Warrior('top'))

# Создание групп синих и красных пуль и списка взрывов
red_bullets_group = pygame.sprite.Group()
blue_bullets_group = pygame.sprite.Group()

# Вспомогательные изменяемые параметры
game_stage = 'battle'
end_screen_delay = Constants.ENDSCREEN_DELAY
explosions = []
winner = None
play_win_sound = True

while True:
    # Закрытие игры при нажатии крестика
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_stage == 'end':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()

    screen.fill('#dcdcdc')
    screen.blit(battlefield, (0, 150))

    # Отрисовка и обновление пуль
    red_bullets_group.draw(screen)
    red_bullets_group.update()
    blue_bullets_group.draw(screen)
    blue_bullets_group.update()

    # Обновление игроков
    red_warrior_group.update()
    blue_warrior_group.update()

    # Получение списков пуль, которые попали
    red_hit_bullets = pygame.sprite.spritecollide(blue_warrior_group.sprite, red_bullets_group, False)
    blue_hit_bullets = pygame.sprite.spritecollide(red_warrior_group.sprite, blue_bullets_group, False)

    if game_stage == 'battle':

        # Обработка выстрелов, если они есть
        blue_shot = blue_warrior_group.sprite.warrior_shots()
        red_shot = red_warrior_group.sprite.warrior_shots()

        if blue_shot != False:
            blue_bullets_group.add(BlueBullet(blue_shot))
        if red_shot != False:
            red_bullets_group.add(RedBullet(red_shot))

        # Если какие-то пули попали, уничтожение их и спавн взрывов
        if red_hit_bullets:
            kill_bullet_and_spawn_explosion()

        if blue_hit_bullets:
            kill_bullet_and_spawn_explosion()

        # Отрисовка игроков
        red_warrior_group.draw(screen)
        blue_warrior_group.draw(screen)

        # Начисление повреждений, если пули попали
        if red_hit_bullets:
            blue_warrior_group.sprite.do_damage(red_hit_bullets)

        if blue_hit_bullets:
            red_warrior_group.sprite.do_damage(blue_hit_bullets)

        # Обработка смертей игроков
        if blue_warrior_group.sprite.heals == 0:
            game_stage = 'end'
            winner = 'red'
            blue_warrior_group.sprite.isAlive = False
            spawn_player_explosion(blue_warrior_group.sprite.rect.centerx,
                                   blue_warrior_group.sprite.rect.centery)

        if red_warrior_group.sprite.heals == 0:
            game_stage = 'end'
            winner = 'blue'
            red_warrior_group.sprite.isAlive = False
            spawn_player_explosion(red_warrior_group.sprite.rect.centerx,
                                   red_warrior_group.sprite.rect.centery)

    elif game_stage == 'end':

        # В двух ветвях происходит отрисовка победителя, обработка пуль противников, определение эндскрина
        # Обработка выстрелов победителя
        if winner == 'red':
            red_warrior_group.draw(screen)
            if blue_hit_bullets:
                kill_bullet_and_spawn_explosion()
            end_screen = red_wins_background

            red_shot = red_warrior_group.sprite.warrior_shots()
            if red_shot != False:
                red_bullets_group.add(RedBullet(red_shot))

        else:
            blue_warrior_group.draw(screen)
            if red_hit_bullets:
                kill_bullet_and_spawn_explosion()
            end_screen = blue_wins_background

            blue_shot = blue_warrior_group.sprite.warrior_shots()
            if blue_shot != False:
                blue_bullets_group.add(BlueBullet(blue_shot))

        # После победы, нужно выждать задержку, после появляется эндскрин, играется звук
        if not end_screen_delay:

            if play_win_sound:
                Sounds.win_sound.play()
            play_win_sound = False

            screen.blit(end_screen, (0, 0))
        else:
            end_screen_delay -= 1

    # Обработка всех взрывов
    if explosions:
        update_explosions()

    pygame.display.update()
    clock.tick(Constants.FPS)
