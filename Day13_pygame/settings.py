class Settings:
    """存储Alien Invasion的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # (135,206,235) # sky blue

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # 子弹设置（单位是像素）
        self.bullet_speed_factor = 1.5
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1  # 右移速度
        self.fleet_drop_speed = 50

        self.fleet_direction = 1  # fleet_direction 为1表示向右移，为-1表示向左移
