import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self,user_settings,screen):
        super().__init__()
        self.screen=screen
        self.user_settings=user_settings

        self.image=pygame.image.load('alien_test/images/star.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height/2

        self.y=float(self.rect.y)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)