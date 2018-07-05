import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船出的位置创建一个子弹对象"""

        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 设置和飞船的x轴位置相同
        self.rect.centerx = ship.rect.centerx
        # 设置和飞船的top位置相同
        self.rect.top = ship.rect.top

        # 存储小数表示的子弹位置
        self.y = float(self.rect.y)

        # 子弹的颜色
        self.color = ai_settings.bullet_color
        # 子弹移动的速度
        self.speed_factor = ai_settings.bullet_speed_factor
    
 
    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        self.rect.y = self.y

 
    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        