import pygame
from pygame.sprite import Sprite

class Player(Sprite):

    def __init__(self,catch_setting,screen):
        super().__init__()
        self.catch_setting=catch_setting
        self.screen=screen

        self.image=pygame.image.load('alien_test/images/user.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.x=float(self.rect.x)

        self.moving_right=False
        self.moving_left=False

    def update(self):

        if self.moving_left and self.rect.left >=0:
            self.x-=self.catch_setting.user_speed_factor

        if self.moving_right and self.rect.right <=self.screen_rect.right:
            self.x+=self.catch_setting.user_speed_factor

        self.rect.x=int(self.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
