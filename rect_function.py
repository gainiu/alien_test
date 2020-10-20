import sys
import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(rect_settings,screen,rectbox):
    screen.fill(rect_settings.screen_bg)
    rectbox.draw_rect()
    pygame.display.flip()