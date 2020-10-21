import pygame


class RectPlayer():

    def __init__(self, rect_settings, screen):
        self.rect_settings = rect_settings
        self.screen = screen

        self.image = pygame.image.load('alien_test/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)

        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.rect_settings.rectplayer_speed
        if self.moving_up and self.rect.y >= 0:
            self.y -= self.rect_settings.rectplayer_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
