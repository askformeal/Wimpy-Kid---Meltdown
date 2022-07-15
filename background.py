import pygame

class Background:
    def __init__(self,main):
        self.screen = main.screen
        self.image = pygame.image.load('background.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def blitme(self):
        self.rect.x = 0
        self.rect.y = 0        
        self.screen.blit(self.image, self.rect)
