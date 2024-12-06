import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50, color=(255, 0, 0)):
        super().__init__()
        # Creates enemy
        """
        Creates enemy class, or what the player is avoiding
        X and Y determine where is is located
        """
        self.image = pygame.Surface((width, height))
        self.image.fill(color) 

        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        