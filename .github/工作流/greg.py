import pygame
# 还有很多事情要做

class Greg:
    def __init__(self,main):
        self.main = main
        self.screen = main.screen

        # 基准图像，其他的都是用pygame.transform.rotate()
        # 所有可能用到的图像都储存在这里备用
        self.image_up = pygame.image.load('greg.bmp')
        self.image_left = pygame.transform.rotate(self.image_up,90)
        self.image_down = pygame.transform.rotate(self.image_up,180)
        self.image_right = pygame.transform.rotate(self.image_up,270)
        self.image_punch = pygame.image.load('greg_punch.bmp')

        # 当前的图像
        self.image = self.image_up
        self.rect = self.image.get_rect()

        # 当前时间（纯粹为了方便）
        self.time = 0

        # 移动速度
        self.speed = 1

        # 方向
        self.direction = 'up'

        # 是否触碰到边缘
        self.up_edge = False
        self.down_edge = False
        self.left_edge = False
        self.right_edge = False

        # 移动时必须加减self.x和self.y，否则会有Bug
        self.x = 0
        self.y = 0

        # 是否在上下左右移动
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        # 暂定出拳时间一秒，冷却时间一秒
        # 是否可以出拳（已出拳时不能出拳，冷却时不能出拳）
        self.punchable = True

        # 出拳开始的时间
        self.punch_start_time = 0

        # 冷却开始时间
        self.cool_down_start_time = 0

        '''
        出拳的原理：
        按下出拳键（q键）时检查punchable是否为True，如果是则切换为出拳动画，punchable改为False，
        punch_start_time设为当前时间。然后在update_punch函数中检查punch_start_time是否不为0，如果是则切换为出拳
        动画，再检查punch_start_time是否距当前时间已有一秒，如果是则重置punch_start_time为0，
        cool_down_start_time设为当前时间，（无需退出出拳动画，其他监测语句会进行更改）。然后监测
        cool_down_start_time是距当前时间已有一秒，如果是则重置cool_down_start_time为0，并将punchable
        设为True。
        '''
        '''
        出拳部分的运行机制非常精妙，所以注释不多。看不懂没关系，因为我也不太懂。如果你想进行任何‘优化’请不要
        删除任何代码并将原版代码做好备份
        '''

    def update_edge(self):
        # 监测是否触碰到边缘
        self.left_edge = self.x <= 0
        # 要减去自身宽度，否则Greg会跑出屏幕边缘（虽然跑不远）
        self.right_edge = self.x >= self.main.screen_wide-self.image.get_width()
        self.up_edge = self.y <= 0
        self.down_edge = self.y >= self.main.screen_high-self.image.get_height()

    def update_direction(self):
         # 设置上下移动方向
        if self.move_up:
            self.direction = 'up'
        elif self.move_down:
            self.direction = 'down'
        elif self.move_left:
            self.direction = 'left'
        elif self.move_right:
            self.direction = 'right'

    def update_move(self):
        # 移动监测
        if self.move_up and not self.up_edge:
            self.y -= self.speed
            self.image = self.image_up

        elif self.move_down and not self.down_edge:
            self.y += self.speed
            self.image = self.image_down

        elif self.move_left and not self.left_edge:
            self.x -= self.speed
            self.image = self.image_left

        elif self.move_right and not self.right_edge:
            self.x += self.speed
            self.image = self.image_right

    def update_punch_image(self):
        # 调整出拳动画方向
        self.image_left = pygame.transform.rotate(self.image_up,90)
        self.image_down = pygame.transform.rotate(self.image_up,180)
        self.image_right = pygame.transform.rotate(self.image_up,270)
        if self.direction == 'down':
            self.image = self.image_down
        elif self.direction == 'left':
            self.image = self.image_left
        elif self.direction == 'right':
            self.image = self.image_right

    def udpate_punch(self):
        # 出拳部分（前面有说明）
        if self.punch_start_time != 0:
            self.update_punch_image()
            self.image_up = self.image_punch
        if self.time - self.punch_start_time >= 0.5 and self.punch_start_time != 0: 
            #                                   ^调整这个数字来设置出拳时间
            self.punch_start_time = 0
            self.cool_down_start_time = self.time
        if self.time - self.cool_down_start_time >= 0.5 and self.cool_down_start_time != 0:
            #                                       ^调整这个数字设置冷却时间
            
            self.cool_down_start_time = 0
            self.image_up = pygame.image.load('greg.bmp')
            self.punchable = True
            self.update_punch_image()
        

    def update(self):
        # 获取当前时间
        self.time = self.main.timer

        # 刷新xy
        self.rect.x = self.x
        self.rect.y = self.y

        self.update_edge()

        self.update_direction()
        self.udpate_punch()
        self.update_move()
        

        

    def blitme(self):        
        self.screen.blit(self.image, self.rect)
