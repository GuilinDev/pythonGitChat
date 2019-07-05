class Settings:
    """存储Alien Invasion的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # (135,206,235) # sky blue

        # 飞船设置
        self.ship_speed_factor = 1.5

        # 子弹设置（单位是像素）
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
