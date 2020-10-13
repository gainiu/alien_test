import pygame

class User():
    def __init__(self,screen,user_settings):
        '''初始化角色并设置其初始位置'''
        self.screen=screen
        self.user_settings=user_settings
        #加载角色图像并获取其外接矩形
        self.image=pygame.image.load('alien_test/images/user.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #将角色放在屏幕中央
        self.rect.right=self.screen_rect.right
        self.rect.centery=self.screen_rect.centery

        self.x=float(self.rect.right)
        self.centery=float(self.rect.centery)

        # self.moving_right=False
        # self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    
    def update(self):
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.centerx+=self.user_settings.user_speed_factor

        # if self.moving_left and self.rect.left > 0:
        #     self.centerx-=self.user_settings.user_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.centery-=self.user_settings.user_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery+=self.user_settings.user_speed_factor

        # self.rect.centerx=self.centerx
        self.rect.centery=self.centery

    def blitme(self):
        '''在指定位置绘制角色'''
        self.screen.blit(self.image,self.rect)