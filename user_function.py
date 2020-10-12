import sys
import pygame

def check_event(user):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                user.moving_right=True
            elif event.key==pygame.K_LEFT:
                user.moving_left=True
            elif event.key==pygame.K_UP:
                user.moving_up=True
            elif event.key==pygame.K_DOWN:
                user.moving_down=True

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                user.moving_right=False
            elif event.key==pygame.K_LEFT:
                user.moving_left=False
            elif event.key==pygame.K_UP:
                user.moving_up=False
            elif event.key==pygame.K_DOWN:
                user.moving_down=False

def upgrade_screen(screen,user,user_settings):
    '''更新屏幕上的图像，并切换到新屏幕'''
    #每次循环都重新绘制屏幕
    screen.fill(user_settings.bg_color)
    user.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()