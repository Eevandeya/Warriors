from Images import screen, battlefield, red_wins_background, blue_wins_background
from Inner import *
import Constants
from Explosions import kill_bullet_and_spawn_explosion, spawn_player_explosion, update_explosions

game_stage = 'battle'
endscreen_delay = Constants.ENDSCREEN_DELAY

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('#dcdcdc')

    screen.blit(battlefield, (0, 150))

    red_bullets_group.draw(screen)
    red_bullets_group.update()

    blue_bullets_group.draw(screen)
    blue_bullets_group.update()

    red_warrior_group.update()

    blue_warrior_group.update()

    red_hit_bullets = pygame.sprite.spritecollide(blue_warrior_group.sprite, red_bullets_group, False)
    blue_hit_bullets = pygame.sprite.spritecollide(red_warrior_group.sprite, blue_bullets_group, False)

    if game_stage == 'battle':

        if red_hit_bullets:
            kill_bullet_and_spawn_explosion()

        if blue_hit_bullets:
            kill_bullet_and_spawn_explosion()

        red_warrior_group.draw(screen)
        blue_warrior_group.draw(screen)

        if red_hit_bullets:
            blue_warrior_group.sprite.do_damage()

        if blue_hit_bullets:
            red_warrior_group.sprite.do_damage()

        if blue_warrior_group.sprite.heals == 0:
            game_stage = 'redWin'
            blue_warrior_group.sprite.isAlive = False
            spawn_player_explosion(blue_warrior_group.sprite.rect.centerx,
                                   blue_warrior_group.sprite.rect.centery)

        if red_warrior_group.sprite.heals == 0:
            game_stage = 'blueWin'
            red_warrior_group.sprite.isAlive = False
            spawn_player_explosion(red_warrior_group.sprite.rect.centerx,
                                   red_warrior_group.sprite.rect.centery)

    elif game_stage == 'redWin':

        red_warrior_group.draw(screen)
        if blue_hit_bullets:
            kill_bullet_and_spawn_explosion()

        if not endscreen_delay:
            screen.blit(red_wins_background, (0,0))
        else:
            endscreen_delay -= 1


    elif game_stage == 'blueWin':

        blue_warrior_group.draw(screen)
        if red_hit_bullets:
            kill_bullet_and_spawn_explosion()

        if not endscreen_delay:
            screen.blit(blue_wins_background, (0,0))
        else:
            endscreen_delay -= 1

    if explosions:
        update_explosions()

    pygame.display.update()
    clock.tick(60)
