import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # 初始化游戏并且创建一个游戏对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 放置一艘飞船
    ship = Ship(ai_settings, screen)

    bullets = Group()
    # 开始游戏地主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()