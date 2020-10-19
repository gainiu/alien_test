import sys
import pygame


def check_keydown_event(event,player):
    if event.key == pygame.K_RIGHT:
        player.moving_right=True
    if event.key == pygame.K_LEFT:
        player.moving_left=True

def check_keyup_event(event,player):
    if event.key ==pygame.K_RIGHT:
        player.moving_right=False
    elif event.key == pygame.K_LEFT:
        player.moving_left=False

def check_event(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,player)

        elif event.type ==pygame.KEYUP:
            check_keyup_event(event,player)

def check_ball_player_collisions(catch_setting,screen,balls,player):
    collisions=pygame.sprite.groupcollide(balls,player,False,True)
    ball=Ball(catch_setting,screen)

def update_ball(catch_setting,screen,balls,player):
    check_ball_player_collisions(catch_setting,screen,balls,player)
    balls.update()

def update_screen(catch_setting,screen,balls,player):
    screen.fill(catch_setting.bg_color)
    player.blitme()
    balls.draw()
    pygame.display.flip()