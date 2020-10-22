import pygame


class Button():

    def __init__(self, rect_settings, screen):
        self.rect_settings = rect_settings
        self.screen = screen
        self.screen_rect=self.screen.get_rect()

        self.font = pygame.font.SysFont(
            None, self.rect_settings.button_fontsize)
        self.rect = pygame.Rect(
            0, 0, self.rect_settings.button_width, self.rect_settings.button_height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(self.rect_settings.button_msg)

    def prep_msg(self, msg):

        self.msg_image = self.font.render(
            msg, True, self.rect_settings.button_text_color, self.rect_settings.button_bg)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        self.screen.fill(self.rect_settings.button_bg,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
