import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Create a surface for the player (50x50 red rectangle as a placeholder)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Fill with red color

        # Create a rectangle for positioning and collision
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Movement attributes
        self.speed = 5

    def move(self, keys):
        # Movement based on key input
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self, keys):
        # Update player position based on keys
        self.move(keys)
