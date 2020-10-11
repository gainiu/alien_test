import sys
import pygame
from settings import Settings
from user import User
import user_function as uf

def run_game():
    '''初始化pygame、设置和屏幕对象'''
    pygame.init()
    user_settings=Settings()
    screen=pygame.display.set_mode((user_settings.screen_width,user_settings.screen_height))
    pygame.display.set_caption('Alien Invasion Test')
    #创建一个角色
    user=User(screen)

    while True:
        '''开始游戏主循环'''
        uf.check_event()
        uf.upgrade_screen(screen,user,user_settings)

run_game()