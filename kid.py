import imp
from random import choice
import pygame
from pygame.sprite import Sprite
from random import randint

# 熊孩子：在屏幕上游走
class Kid(Sprite):
    def __init__(self,main):
        super().__init__()
        self.screen = main.screen
        self.image = pygame.image.load('kid.bmp')
        self.rect = self.image.get_rect()
        self.x = randint(0,main.screen_wide)
        self.y = randint(0,main.screen_high)
        self.main = main
        #实体
        self.mobs = self.main.mobs
        #目标：攻击对象
        self.target = None

    def update(self):
        self.time = self.main.timer
        self.rect.x = self.x
        self.rect.y = self.y
        if self.time % 2 == 0:
            self.mobs = self.main.mobs
            self.mobs.remove(self)
            #随机目标
            self.target = choice(self.mobs)

