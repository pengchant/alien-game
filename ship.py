import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings, screen):                
        """初始化飞船的位置"""

        super().__init__()

        self.screen = screen
        
        self.ai_settings = ai_settings 

        # 设置飞船的图片
        self.image = pygame.image.load('./images/ship.bmp')
        # 获取飞船的大小
        self.rect = self.image.get_rect()
        # 获取真个屏幕的大小
        self.screen_rect = screen.get_rect()

        # 将宇宙飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
        # 设置位置变化
        self.center = float(self.rect.centerx)
        
    def blitme(self):
        """在屏幕上绘制宇宙飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center跟新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx