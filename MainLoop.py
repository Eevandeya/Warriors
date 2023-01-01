import pygame
from Screen import screen, battlefield, end_screen_backround, \
    choosing_field, win_fount, names
from Warrior import Warrior
import Constants
from Bullet import RedBullet, BlueBullet
import Sounds
import Explosions
from PickingPanel import PickingPanel


def kill_bullet_and_spawn_explosions():
    red_dead = False
    blue_dead = False

    for bullet in blue_hit_bullets:
        if red_warrior_group.sprite.heals == 0:
            explosions.append(Explosions.PlayerExplosion(red_warrior_group.sprite.rect.centerx,
                                                         red_warrior_group.sprite.rect.centery))
            red_warrior_group.sprite.death_sound.play()
            red_dead = True

        else:
            explosions.append(Explosions.BulletExplosion(bullet.rect.x, bullet.rect.y))
            red_warrior_group.sprite.hit_sound.play()

        bullet.kill()

    for bullet in red_hit_bullets:
        if blue_warrior_group.sprite.heals == 0:
            explosions.append(Explosions.PlayerExplosion(blue_warrior_group.sprite.rect.centerx,
                                                         blue_warrior_group.sprite.rect.centery))
            blue_warrior_group.sprite.death_sound.play()
            blue_dead = True

        else:
            explosions.append(Explosions.BulletExplosion(bullet.rect.x, bullet.rect.y))
            blue_warrior_group.sprite.hit_sound.play()

        bullet.kill()

    return red_dead, blue_dead

def update_explosions():
    for explosion in explosions:
        isdead = explosion.update()
        if isdead:
            explosions.remove(explosion)


def spawn_player_explosion(x, y):
    explosions.append(Explosions.PlayerExplosion(x, y))
    if not blue_warrior_group.sprite.isAlive:
        blue_warrior_group.sprite.death_sound.play()
    else:
        red_warrior_group.sprite.death_sound.play()


def reset_game():
    blue_warrior_group.empty()
    red_warrior_group.empty()

    red_bullets_group = pygame.sprite.Group()
    blue_bullets_group = pygame.sprite.Group()

    game_stage = 'pick'
    end_screen_delay = Constants.ENDSCREEN_DELAY
    explosions = []
    winner = None
    play_win_sound = True

    top_pick_panel = PickingPanel('top')
    bottom_pick_panel = PickingPanel('bottom')
    start_timer = 100
    countdown = False
    isRedDead, isBlueDead = False, False

    globals().update(locals())


pygame.init()

clock = pygame.time.Clock()

blue_warrior_group = pygame.sprite.GroupSingle()
red_warrior_group = pygame.sprite.GroupSingle()

# Создание групп синих и красных пуль и списка взрывов
red_bullets_group = pygame.sprite.Group()
blue_bullets_group = pygame.sprite.Group()

# Вспомогательные изменяемые параметры
game_stage = 'pick'
end_screen_delay = Constants.ENDSCREEN_DELAY
explosions = []
winner = None
play_win_sound = True

top_pick_panel = PickingPanel('top')
bottom_pick_panel = PickingPanel('bottom')
start_timer = 100
countdown = False
isRedDead, isBlueDead = False, False

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

    if game_stage == 'pick':
        screen.blit(choosing_field, (0, 0))
        top_pick_panel.update()
        bottom_pick_panel.update()

        if top_pick_panel.picked and bottom_pick_panel.picked and not countdown:
            countdown = True
            # Создание группы синего игрока
            red_warrior_group.add(Warrior('bottom', bottom_pick_panel.pointer))
            blue_warrior_group.add(Warrior('top', top_pick_panel.pointer))

        if countdown:
            start_timer -= 1

        if not start_timer:
            game_stage = 'battle'

    else:
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

            # Если какие-то пули попали, уничтожение их, спавн взрывов
            # и начисление повреждений игрокам
            if red_hit_bullets or blue_hit_bullets:

                if red_hit_bullets:
                    blue_warrior_group.sprite.do_damage(len(red_hit_bullets))

                if blue_hit_bullets:
                    red_warrior_group.sprite.do_damage(len(blue_hit_bullets))

                isRedDead, isBlueDead = kill_bullet_and_spawn_explosions()
                print(isRedDead, isBlueDead)

            # Отрисовка игроков
            red_warrior_group.draw(screen)
            blue_warrior_group.draw(screen)

            # Обработка смертей игроков
            if isBlueDead:
                game_stage = 'end'
                winner = 'red'
                blue_warrior_group.sprite.isAlive = False

            if isRedDead:
                game_stage = 'end'
                winner = 'blue'
                red_warrior_group.sprite.isAlive = False

        elif game_stage == 'end':

            # В двух ветвях происходит отрисовка победителя, обработка пуль противников, определение эндскрина
            # Обработка выстрелов победителя
            if winner == 'red':
                red_warrior_group.draw(screen)
                if blue_hit_bullets:
                    kill_bullet_and_spawn_explosions()

                winner_num = red_warrior_group.sprite.character
                end_screen = end_screen_backround
                winner_name = win_fount.render(names[winner_num], False, Constants.RED)
                wins_word = win_fount.render('wins', False, Constants.BLACK)

                red_shot = red_warrior_group.sprite.warrior_shots()
                if red_shot != False:
                    red_bullets_group.add(RedBullet(red_shot))

            else:
                blue_warrior_group.draw(screen)
                if red_hit_bullets:
                    kill_bullet_and_spawn_explosions()

                winner_num = blue_warrior_group.sprite.character
                end_screen = end_screen_backround
                winner_name = win_fount.render(names[winner_num], False, Constants.BLUE)
                wins_word = win_fount.render('wins', False, Constants.BLACK)

                blue_shot = blue_warrior_group.sprite.warrior_shots()
                if blue_shot != False:
                    blue_bullets_group.add(BlueBullet(blue_shot))

            # После победы, нужно выждать задержку, после появляется эндскрин, играется звук
            if not end_screen_delay:

                if play_win_sound:
                    Sounds.win_sound.play()
                play_win_sound = False

                screen.blit(end_screen, (0, 0))
                screen.blit(winner_name, (Constants.WINNER_XS[winner_num], Constants.WINNER_NAME_Y))
                screen.blit(wins_word, (Constants.WINS_WORD_X, Constants.WINS_WORD_Y))
            else:
                end_screen_delay -= 1

        # Обработка всех взрывов
        if explosions:
            update_explosions()

    pygame.display.update()
    clock.tick(Constants.FPS)
