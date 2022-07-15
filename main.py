'''
NO BUGS

    BBBBBBBBBBBBBBB       UUUU             UUUU             GGGG
    BBBBBBBBBBBBBBBB      UUUU             UUUU          GGGGGGGGGG
    BBBB         BBBB     UUUU             UUUU        GGGG       GGGG
    BBBB         BBBB     UUUU             UUUU       GGGG         GGGG
    BBBB         BBBB     UUUU             UUUU      GGGG           GGGG
    BBBB        BBB       UUUU             UUUU     GGGG            
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 
    BBBB        BBB       UUUU             UUUU     GGGG          GGGGGGGGGGG
    BBBB         BBBB     UUUU             UUUU      GGGG         GGGGGG  GGGG
    BBBB         BBBB     UUUUU           UUUUU       GGGG         GGGG   GGGG
    BBBB         BBBB      UUUUU         UUUUU         GGGG       GGGG
    BBBBBBBBBBBBBBBB        UUUUUUUUUUUUUUUUU            GGGGGGGGGG
    BBBBBBBBBBBBBBB           UUUUUUUUUUUUU                 GGGG   
'''

import pygame
import sys
import time

from background import Background
from greg import Greg
from snowball import Snowball

class Main:
    def __init__(self):
        pygame.init()
        self.screen_high = 522
        self.screen_wide = 1341
        self.screen = pygame.display.set_mode((self.screen_wide,self.screen_high))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(f"---|Diary of a Wimpy Kid: The Meltdown|---")

        # 计时器，用于进行等待等操作
        self.start = time.time() # 纪录程序开始的时间
        self.timer = 0

        # 背景对象
        self.background = Background(self)
        # Greg对象
        self.greg = Greg(self)
        # 雪球对象
        self.snowballs = pygame.sprite.Group()

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event.key)                   
            elif event.type == pygame.KEYUP:
                self._check_keyup(event.key)

    def _check_keydown(self,event):
        # WASD键控制Greg的移动
        if event == pygame.K_w:
            self.greg.move_up = True
        elif event == pygame.K_s:
            self.greg.move_down = True
        elif event == pygame.K_a:
            self.greg.move_left = True
        elif event == pygame.K_d:
            self.greg.move_right = True
        # e键投雪球
        elif event == pygame.K_e:
            new_ball = Snowball(self.greg.direction,self)
            self.snowballs.add(new_ball)

        # q键出拳，详见greg.py
        elif event == pygame.K_q and self.greg.punchable:
            self.greg.punchable = False
            self.greg.punch_start_time = self.timer

        # 测试键，正式版要删掉
        elif event == pygame.K_SPACE:
            print(f'timer:{self.timer}')
        # esc键退出
        elif event == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup(self,event):
        # WASD键控制Greg不移动
        if event == pygame.K_w:
            self.greg.move_up = False
        elif event == pygame.K_s:
            self.greg.move_down = False
        elif event == pygame.K_a:
            self.greg.move_left = False
        elif event == pygame.K_d:
            self.greg.move_right = False

    #刷新雪球
    def update_snowballs(self):
        self.snowballs.update()
        self.snowballs.draw(self.screen)
        for snowball in self.snowballs.sprites():
            # 监测是否触碰到边缘
            left_edge = snowball.x <= 0
            right_edge = snowball.x >= self.screen_wide
            up_edge = snowball.y <= 0
            down_edge = snowball.y >= self.screen_high
            if left_edge or right_edge or up_edge or down_edge:
                self.snowballs.remove(snowball)

    # 刷新计时器
    def update_timer(self):
        self.timer = time.time() - self.start
        # 四舍五入到整数
        self.timer = round(self.timer,1)

    def update(self):
        # 刷新背景
        self.background.blitme()

        # 刷新Greg ^_^
        self.greg.blitme()
        self.greg.update()

        # 刷新雪球
        self.update_snowballs()

        # 刷新计时器
        self.update_timer()

        pygame.display.flip()
        
    def run_game(self):
        while True:
            self.update()
            self.check()

if __name__ == '__main__':
    main = Main()
    main.run_game()
