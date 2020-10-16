import sys
import pygame
from bullet import Bullet
from star import Star
from random import randint

def check_keydown_event(event,user,user_settings,screen,bullets):
    # if event.key==pygame.K_RIGHT:
    #     user.moving_right=True
    # elif event.key==pygame.K_LEFT:
    #     user.moving_left=True
    if event.key==pygame.K_UP:
        user.moving_up=True
    elif event.key==pygame.K_DOWN:
        user.moving_down=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(user,user_settings,screen,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def fire_bullet(user,user_settings,screen,bullets):
    if len(bullets) < user_settings.bullet_allowed:
        new_bullet=Bullet(user_settings,screen,user)
        bullets.add(new_bullet)

def check_keyup_event(event,user):
    # if event.key==pygame.K_RIGHT:
    #     user.moving_right=False
    # elif event.key==pygame.K_LEFT:
    #     user.moving_left=False
    if event.key==pygame.K_UP:
        user.moving_up=False
    elif event.key==pygame.K_DOWN:
        user.moving_down=False

def check_event(user,user_settings,screen,bullets):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_event(event,user,user_settings,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_event(event,user)

def upgrade_screen(screen,user,user_settings,bullets,stars):
    '''更新屏幕上的图像，并切换到新屏幕'''
    
    #每次循环都重新绘制屏幕
    screen.fill(user_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    user.blitme()
    stars.draw(screen)
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullet(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right <=0:
            bullets.remove(bullet)

def create_fleet(user_settings,screen,stars,user):
    star=Star(user_settings,screen)
    number_star_y=get_number_stars_y(user_settings,star.rect.height)
    number_rows=get_number_rows(user_settings,star.rect.width,user.rect.width)

    for row_number in range(number_rows):
        for star_number in range(number_star_y):
            create_star(user_settings,screen,stars,randint(-1,star_number),randint(-1,row_number))

def get_number_stars_y(user_settings,star_height):
    available_space_y=user_settings.screen_height-star_height
    number_star_y=int(available_space_y/(2*star_height))
    return number_star_y

def create_star(user_settings,screen,stars,star_number,row_number):
    star=Star(user_settings,screen)
    star_height=star.rect.height
    star.y=(star_height/2)+(2*star_height*star_number)
    star.rect.y=star.y
    star.rect.x=star.rect.width+2*star.rect.width*row_number
    stars.add(star)

def get_number_rows(user_settings,star_width,user_width):
    available_space_x=user_settings.screen_width-(3*star_width)-user_width
    number_rows=int(available_space_x/(2*star_width))
    return number_rows
