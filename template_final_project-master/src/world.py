import pygame
class World(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)