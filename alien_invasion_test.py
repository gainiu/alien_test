import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from user import User
from star import Star
import user_function as uf

def run_game():
    '''初始化pygame、设置和屏幕对象'''
    pygame.init()
    user_settings=Settings()
    screen=pygame.display.set_mode((user_settings.screen_width,user_settings.screen_height))
    pygame.display.set_caption('Alien Invasion Test')
    #创建一个角色
    user=User(screen,user_settings)

    bullets=Group()

    stars=Group()
    uf.create_fleet(user_settings,screen,stars,user)

    while True:
        '''开始游戏主循环'''
        uf.check_event(user,user_settings,screen,bullets)
        user.update()
        uf.update_bullet(bullets)
        uf.upgrade_screen(screen,user,user_settings,bullets,stars)

run_game()