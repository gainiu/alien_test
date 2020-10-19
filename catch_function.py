import sys
import pygame
from ball import Ball
from player import Player

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
def hit_edge():
    pass

def check_ball_player_collisions(catch_setting,screen,balls,players,stats):
    collisions=pygame.sprite.groupcollide(balls,players,True,False)
    if len(balls)==0:
        balls.empty()
        create_balls(catch_setting,screen,balls)
    
    for ball in balls:
        if ball.rect.y==catch_setting.screen_height:
            stats.player_left-=1
            balls.empty()
            create_balls(catch_setting,screen,balls)
            break

def create_balls(catch_setting,screen,balls):
    ball=Ball(catch_setting,screen)
    balls.add(ball)

def update_ball(catch_setting,screen,balls,players,stats):  
    balls.update()
    if stats.player_left > 0:
        check_ball_player_collisions(catch_setting,screen,balls,players,stats)
    else:
        stats.game_active=False

def create_players(catch_setting,screen,players):
    player=Player(catch_setting,screen)
    players.add(player)

def update_screen(catch_setting,screen,balls,player):
    screen.fill(catch_setting.bg_color)
    player.draw(screen)
    balls.draw(screen)
    pygame.display.flip()