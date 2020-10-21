import pygame
from pygame.sprite import Sprite

class RectBullet(Sprite):

    def __init__(self,rect_settings,screen,rectplayer):
        super().__init__()
        self.rect_settings=rect_settings
        self.screen=screen

        self.rect=pygame.Rect(0,0,self.rect_settings.bullet_width,self.rect_settings.bullet_height)
        self.rect.centery=rectplayer.rect.centery
        self.rect.right=rectplayer.rect.right

        self.x=float(self.rect.x)

        self.color=self.rect_settings.bullet_bg
        self.speed=self.rect_settings.bullet_speed_factor

    def update(self):
        self.x+=self.speed
        self.rect.x=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
