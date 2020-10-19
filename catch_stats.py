class  CatchStats():
    
    def __init__(self,catch_setting):
        self.catch_setting=catch_setting
        self.reset_stats()
        self.game_active=True

    def reset_stats(self):
        self.player_left=self.catch_setting.player_limit