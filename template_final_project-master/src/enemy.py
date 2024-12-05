import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50, color=(255, 0, 0)):
        super().__init__()
        # Create a surface for the enemy
        self.image = pygame.Surface((width, height))
        self.image.fill(color)  # Default color is red

        # Create a rectangle for positioning and collision
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)