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

        # State flags
        self.on_ground = False  # Tracks if the player is on the ground or a platform
        self.jump_pressed = False  # Tracks if the jump key is currently pressed

    def move(self, keys, worlds):
        # Horizontal movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.check_horizontal_collision(worlds)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.check_horizontal_collision(worlds)

    def check_horizontal_collision(self, worlds):
        # Prevent the player from moving through world pieces horizontally
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
        self.on_ground = False  # Assume player is in the air unless a collision occurs

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
        # Jump only if on the ground and the jump key was not previously pressed
        if keys[pygame.K_SPACE] and self.on_ground and not self.jump_pressed:
            self.y_velocity = self.jump_strength
            self.on_ground = False  # Player is now airborne
            self.jump_pressed = True  # Mark the jump key as pressed

        # Reset the jump flag when the space key is released
        if not keys[pygame.K_SPACE]:
            self.jump_pressed = False

    def update(self, keys, worlds):
        # Update player position based on keys
        self.move(keys, worlds)
        self.apply_gravity()
        self.check_vertical_collision(worlds)
        self.check_horizontal_collision(worlds)
        self.jump(keys)
