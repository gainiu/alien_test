import pygame
from random import randint

class Ball():

    def __init__(self,catch_setting,screen):
        self.catch_setting=catch_setting
        self.screen=screen

        self.image=pygame.image.load('images/ball.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.centerx=randint(0,self.catch_setting.screen_width)
        self.y=self.rect.y

    def update(self):
        self.y+=self.catch_setting.ball_speed_factor
        self.rect.y=self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)