import sys
import pygame

from settings.settings import Settings
from role.ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    init_settings = Settings()
    screen = pygame.display.set_mode((init_settings.screen_width, init_settings.screen_height))
    pygame.display.set_caption('XX游戏')

    ship = Ship(screen)
    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环绘制背景
        screen.fill(init_settings.bg_color)
        ship.blit_me()
        # 让最近绘制屏幕可见
        pygame.display.flip()


run_game()
