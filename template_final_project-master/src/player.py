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
        self.y_velocity = 0  # Vertical speed
        self.gravity = 0.5  # Force pulling the player down
        self.jump_strength = -10  # Jumping force

        # Ground level (for simplicity, assume the ground is at y=550)
        self.ground_level = 550
    def move(self, keys):
        # Movement based on key input
       
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
    def the_gravity(self,worlds):
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        ##Dont go thru ground
        if self.rect.bottom > self.ground_level:
            self.rect.bottom = self.ground_level
            self.y_velocity = 0  # Reset vertical velocity when on the ground
        
        for world in worlds:
            if self.rect.colliderect(world.rect) and self.y_velocity >= 0:
                self.rect.bottom = world.rect.top
                self.y_velocity = 0  # Stop falling when on a platform
                break
    def jump(self,keys):
        # Jump only if on the ground
        if keys[pygame.K_SPACE] and self.rect.bottom == self.ground_level:
            self.y_velocity = self.jump_strength
    def update(self, keys, worlds):
        # Update player position based on keys
        self.move(keys)
        self.the_gravity(worlds)
        self.jump(keys)