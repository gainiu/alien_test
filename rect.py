import pygame
from pygame.sprite import Sprite


class RectBox(Sprite):

    def __init__(self, rect_settings, screen):
        super().__init__()
        self.rect_settings = rect_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(
            0, 0, self.rect_settings.rect_width, self.rect_settings.rect_height)
        self.rect.right = self.screen_rect.right

        self.y =float(self.rect.y)

        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_down:
            self.y+=self.rect_settings.rect_speed_factor
        if self.moving_up:
            self.y-=self.rect_settings.rect_speed_factor

        self.rect.y=self.y

    def draw_rect(self):
        pygame.draw.rect(
            self.screen, self.rect_settings.rect_color, self.rect, 0)
