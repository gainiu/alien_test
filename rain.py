import pygame
from pygame.sprite import Sprite


class Rain(Sprite):

    def __init__(self, rain_setting, screen):
        super().__init__()
        self.rain_setting = rain_setting
        self.screen = screen

        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()
        # self.screen_rect=self.screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


    def blitme(self):
        self.screen.blit(self.image,self.rect)
