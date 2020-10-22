class RectStats():
    
    def __init__(self,rect_settings):
        self.rect_settings=rect_settings
        self.rect_active=False
        self.reset_stats()

    def reset_stats(self):
        self.rect_left=self.rect_settings.rectplayer_limit