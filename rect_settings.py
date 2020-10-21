import pygame


class RectSettings():

    def __init__(self):

        self.screen_width = 1024
        self.screen_height = 500
        self.screen_bg = (230, 230, 230)

        self.rect_width = 50
        self.rect_height = 50
        self.rect_color = (0, 0, 0)
        self.rect_speed_factor = 1

        self.rectplayer_speed = 1
        self.rectplayer_limit=3

        self.bullet_width=15
        self.bullet_height=3
        self.bullet_bg=(60,60,60)
        self.bullet_speed_factor=1
