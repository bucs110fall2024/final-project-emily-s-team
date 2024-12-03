import pygame
class World(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.image.load("assets/ground background.png")
        self.image = pygame.transform.scale(self.image, (width, height))  # Scale image to platform size
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)