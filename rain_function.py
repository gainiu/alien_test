import sys
import pygame
from pygame.sprite import Sprite
from rain import Rain
import random


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def create_fleet(rain_setting,screen,rains):
    rain=Rain(rain_setting,screen)
    number_rain_x=get_number_rain_x(rain_setting,rain)

    for rain_number in range(number_rain_x):
        create_rain(rain_setting,screen,rains,rain_number)

def get_number_rain_x(rain_setting,rain):
    rain_width=rain.rect.width
    available_space_x=rain_setting.screen_width-rain_width
    number_rain_x=int(available_space_x/(2*rain_width))
    return number_rain_x

def create_rain(rain_setting,screen,rains,rain_number):
    rain=Rain(rain_setting,screen)
    rain_width=rain.rect.width
    rain.x=rain_width+2*rain_width*rain_number
    rain.rect.x=rain.x
    rains.add(rain)

def update_screen(rain_setting, screen, rains):
    screen.fill(rain_setting.screen_bg_color)
    rains.draw(screen)
    pygame.display.flip()

def change_fleet_direction(rain_setting,rains):
    for rain in rains.sprites():
        rain.y=float(rain.rect.y)
        rain.y+=random.uniform(0,rain_setting.fleet_drop_speed)
        rain.rect.y=rain.y

def update_rain(rain_setting,screen,rains):
    change_fleet_direction(rain_setting,rains)
    check_rain_bottom(rain_setting,screen,rains)

def check_rain_bottom(rain_setting,screen,rains):
    screen_rect=screen.get_rect()
    for rain in rains.sprites():
        if rain.rect.bottom >= screen_rect.bottom:
            rains.empty()
            create_fleet(rain_setting,screen,rains)