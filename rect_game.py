import sys
import pygame
from pygame.sprite import Group
from rect_settings import RectSettings
from rect import RectBox
from rect_player import RectPlayer
from rect_bullet import RectBullet
import rect_function as rf


def run_time():

    pygame.init()
    rect_settings = RectSettings()
    screen = pygame.display.set_mode(
        (rect_settings.screen_width, rect_settings.screen_height))
    pygame.display.set_caption('RectGame')

    rectplayer = RectPlayer(rect_settings, screen)

    rectbullets=Group()
    rectboxes=Group()

    while True:

        rf.check_event(rect_settings,screen, rectplayer, rectbullets)
        rf.update_rectbox(rect_settings, screen, rectboxes,rectbullets)
        rf.update_bullet(rectbullets,screen)
        rf.update_screen(rect_settings, screen, rectboxes, rectplayer, rectbullets)


run_time()
