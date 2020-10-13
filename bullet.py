import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,user_settings,screen,user):
        super().__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0,user_settings.bullet_width,user_settings.bullet_height)
        self.rect.left=user.rect.left
        self.rect.centery=user.rect.centery

        self.color=user_settings.bullet_color
        self.speed_factor=user_settings.bullet_speed_factor

        self.x=float(self.rect.x)

    def update(self):
        self.x-=self.speed_factor
        self.rect.centerx=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)