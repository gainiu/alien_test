import pygame


class RectSettings():

    def __init__(self):

        self.screen_width = 1024
        self.screen_height = 500
        self.screen_bg = (230, 230, 230)

        self.rect_width = 50
        self.rect_height = 50
        self.rect_color = (0, 0, 0)

        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_bg = (60, 60, 60)

        self.button_width = 200
        self.button_height = 50
        self.button_bg = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.button_fontsize = 48
        self.button_msg = 'PLAY'

        self.speedup_scale = 1.5
        self.initial_dynamic_settings()

    def initial_dynamic_settings(self):
        self.rect_speed_factor = 1
        self.rectplayer_speed = 1
        self.bullet_speed_factor = 2
        self.rectplayer_limit = 3

    def increase_speed(self):
        self.rect_speed_factor *= self.speedup_scale
        self.rectplayer_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
