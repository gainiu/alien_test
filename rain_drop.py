import sys
import pygame
from pygame.sprite import Group
from rain_settings import RainSettings
from rain import Rain
import rain_function as rf

def run_time():
    pygame.init()
    rain_setting=RainSettings()
    screen = pygame.display.set_mode((rain_setting.screen_width,rain_setting.screen_height))
    pygame.display.set_caption('Rain Drop')

    # rain=Rain(rain_setting,screen)
    rains=Group()

    rf.create_fleet(rain_setting,screen,rains)

    while True:
        
        rf.check_events()
        rf.update_rain(rain_setting,screen,rains)
        rf.update_screen(rain_setting,screen,rains)
        

run_time()
