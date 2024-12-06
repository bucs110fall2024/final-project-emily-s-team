import pygame
class World(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        """
        Creates the platforms and world that player can move around
        X, Y, Width, And Height can be used to create the size and location of platform
        """
        self.image = pygame.Surface((width, height))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)