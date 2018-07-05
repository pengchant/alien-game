import pygame.font

class Button():
    """自定义的button类"""

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮"""    
        
        # 获取屏幕
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arial', 48)

        # 创建按钮的rect对象， 并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """按钮的标签"""

        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
