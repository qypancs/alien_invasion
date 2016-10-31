import sys
import pygame

def run_game():
    # 初始化游戏并且创建一个游戏对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色
    bg_color = (230, 230, 230)

    # 开始游戏地主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制地屏幕可见
        pygame.display.flip()

run_game()