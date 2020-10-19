import sys
import pygame
from catch_settings import CatchBall
from player import Player
from ball import Ball
import catch_function as cf

from pygame.sprite import Group

def run_time():
    pygame.init()
    catch_setting=CatchBall()
    screen=pygame.display.set_mode((catch_setting.screen_width,catch_setting.screen_height))
    pygame.display.set_caption('Catch Ball')

    player=Player(catch_setting,screen)
    # ball=Ball(catch_setting,screen)
    balls=Group()

    while True:
        
        cf.check_event(player)
        player.update()
        cf.update_ball(catch_setting,screen,balls,player)
        cf.update_screen(catch_setting,screen,balls,player)

run_time()