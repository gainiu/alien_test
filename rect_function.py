import sys
import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_rectbox(rect_settings,screen,rectbox):
    screen_rect=screen.get_rect()
    if rectbox.rect.bottom >= screen_rect.bottom:
        rect_settings.rect_speed_factor*=-1
    elif rectbox.rect.top <=0:
        rect_settings.rect_speed_factor*=1
    rectbox.update()

def update_screen(rect_settings,screen,rectbox):
    screen.fill(rect_settings.screen_bg)
    rectbox.draw_rect()
    pygame.display.flip()