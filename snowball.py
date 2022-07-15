from turtle import update
import pygame
from pygame.sprite import Sprite

class Snowball(Sprite):
    # direction是元组，元素1代表上下，-1是上0不动1是下。元素2代表左右，-1是左0不动1是右
    # My ass！他是个列表！！！
    def __init__(self,direction,main):
        super().__init__()
        self.direction = direction
        self.screen = main.screen
        self.image = pygame.image.load('snowball.bmp')
        self.rect = self.image.get_rect()
        self.x = main.greg.rect.center[0]
        self.y = main.greg.rect.center[1]

    def blitme(self):        
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 如果你看不懂就别看了
        self.rect.x = self.x
        self.rect.y = self.y

        
        # 根据Greg的方向移动雪球
        if self.direction == 'up':
            self.y -= 2
        elif self.direction == 'down':
            self.y += 2
        elif self.direction == 'left':
            self.x -= 2
        elif self.direction == 'right':
            self.x += 2
