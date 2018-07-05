import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_status import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # 游戏初始化
    pygame.init()
   
    # 获取相关配置
    ai_settings = Settings()

    # 获取游戏主屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    ) 

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    # 创造一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一行外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于游戏统计的实例
    stats = GameStats(ai_settings)

    # 创建一个button
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏统计信息实例
    sb = ScoreBoard(ai_settings, screen, stats)

    # 开始主循环
    while True:
        # 监听事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 改动飞船位置
            ship.update() 
            # 更改子弹位置(同时检测碰撞)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) 
            # 更改外星人的位置
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        else:
            pygame.mouse.set_visible(True)
      
        # 重新绘制页面
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button);

# 启动游戏
run_game()