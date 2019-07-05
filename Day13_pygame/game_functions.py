import sys, pygame

"""
存储让游戏运行的函数
简化run_game()并隔离事件管理循环
"""


def check_events():
    """响应按键和鼠标事件"""

    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 单机游戏窗口关闭按钮等事件
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 绘制一个空屏幕，并擦去旧屏幕，不管更新屏幕让最近绘制的屏幕可见，营造平移滑动的的效果
    pygame.display.flip()
