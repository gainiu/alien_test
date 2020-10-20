import sys
import pygame
from rect_settings import RectSettings
from rect import RectBox
import rect_function as rf

def run_time():

    pygame.init()
    rect_settings=RectSettings()
    screen = pygame.display.set_mode((rect_settings.screen_width,rect_settings.screen_height))
    pygame.display.set_caption('RectGame')

    rectbox=RectBox(rect_settings,screen)

    while True:

        rf.check_event()       
        rf.update_screen(rect_settings,screen,rectbox)
        

run_time()