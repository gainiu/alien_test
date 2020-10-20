import pygame

class RectBox():

    def __init__(self,rect_settings,screen):
        self.rect_settings=rect_settings
        self.screen=screen
        self.screen_rect=self.screen.get_rect()

        self.rect=pygame.Rect(0,0,self.rect_settings.rect_width,self.rect_settings.rect_height)
        self.rect.right=self.screen_rect.right

    def draw_rect(self):
        pygame.draw.rect(self.screen,self.rect_settings.rect_color,self.rect,0)