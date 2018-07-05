class Settings():
    """存储《外星人入侵》所有设置的类"""
    
    def __init__(self):
        """初始化屏幕设置"""

        # 画布的配置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # 飞船的设置
        self.ship_speed_factor = 1.6
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30

        # 外星人的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 1
        self.fleet_direction = 1

        # 加速
        self.speedup_scale = 1.1

        self.score_scale = 1.5

        # 记分
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """初始化随游戏而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points *= self.score_scale 
        



    