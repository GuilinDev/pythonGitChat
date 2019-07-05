import sys, pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    # 对象screen是一个 surface。在 Pygame 中，surface 是屏幕的一部分，用于显示游戏元素
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # 参数是元组

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()
