import sys
import pygame
from catch_settings import CatchBall
from player import Player
from ball import Ball
from catch_stats import CatchStats
import catch_function as cf

from pygame.sprite import Group

def run_time():
    pygame.init()
    catch_setting=CatchBall()
    screen=pygame.display.set_mode((catch_setting.screen_width,catch_setting.screen_height))
    pygame.display.set_caption('Catch Ball')

    # player=Player(catch_setting,screen)
    # ball=Ball(catch_setting,screen)
    players=Group()
    cf.create_players(catch_setting,screen,players)

    balls=Group()
    cf.create_balls(catch_setting,screen,balls)

    stats=CatchStats(catch_setting)

    while True:
        
        for player in players:
            cf.check_event(player)
        if stats.game_active:
            players.update()
            cf.update_ball(catch_setting,screen,balls,players,stats)
        cf.update_screen(catch_setting,screen,balls,players)

run_time()