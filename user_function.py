import sys
import pygame

def check_event():
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

def upgrade_screen(screen,user,user_settings):
    '''更新屏幕上的图像，并切换到新屏幕'''
    #每次循环都重新绘制屏幕
    screen.fill(user_settings.bg_color)
    user.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()