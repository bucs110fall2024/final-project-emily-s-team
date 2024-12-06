import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Create the player surface
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Fill with red color

        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Movement attributes
        self.speed = 5
        self.y_velocity = 0  
        self.gravity = 0.5  
        self.jump_strength = -10  

        
        self.on_ground = False  
        self.jump_pressed = False  

    def move(self, keys, worlds):
        # Horizontal movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.check_horizontal_collision(worlds)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.check_horizontal_collision(worlds)

    def check_horizontal_collision(self, worlds):
        # PLayer can't walk through walls
        for world in worlds:
            if self.rect.colliderect(world.rect):
                if self.rect.right > world.rect.left and self.rect.centerx < world.rect.centerx:
                    self.rect.right = world.rect.left  # Prevent moving right through
                elif self.rect.left < world.rect.right and self.rect.centerx > world.rect.centerx:
                    self.rect.left = world.rect.right  # Prevent moving left through

    def apply_gravity(self):
        # Apply gravity
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        self.on_ground = False  

    def check_vertical_collision(self, worlds):
        for world in worlds:
            if self.rect.colliderect(world.rect):
                if self.y_velocity > 0:  # Falling
                    self.rect.bottom = world.rect.top
                    self.y_velocity = 0
                    self.on_ground = True
                elif self.y_velocity < 0:  # Jumping up
                    self.rect.top = world.rect.bottom
                    self.y_velocity = 0

    def jump(self, keys):
        # Prevents jumping in air / double jumping
        if keys[pygame.K_SPACE] and self.on_ground and not self.jump_pressed:
            self.y_velocity = self.jump_strength
            self.on_ground = False  
            self.jump_pressed = True  

        # Makes it so when jump is not pressed, flag is reset
        if not keys[pygame.K_SPACE]:
            self.jump_pressed = False

    def update(self, keys, worlds):
        # Updates
        self.move(keys, worlds)
        self.apply_gravity()
        self.check_vertical_collision(worlds)
        self.check_horizontal_collision(worlds)
        self.jump(keys)
