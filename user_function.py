import sys
import pygame
from bullet import Bullet
from star import Star

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

def create_fleet(user_settings,screen,stars):
    star=Star(user_settings,screen)
    star_height=star.rect.height
    available_space_y=user_settings.screen_height-star_height
    number_star_y=int(available_space_y/(2*star_height))

    for star_number in range(number_star_y):
        star=Star(user_settings,screen)
        star.y=(star_height/2)+(2*star_height*star_number)
        star.rect.y=star.y
        stars.add(star)