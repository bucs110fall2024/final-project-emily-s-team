import pygame
from src.player import Player

class Controller:
    def __init__(self):
        # Initialize controller variables
        self.screen = None
        self.clock = None
        self.running = True
        self.state = "menu"

    def mainloop(self):
        # Setup screen and clock
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Initialize player and sprite groups
        player = Player(375, 275)  # Starting position near the center
        all_sprites = pygame.sprite.Group()  # Create the sprite group
        all_sprites.add(player)

        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Get pressed keys
            keys = pygame.key.get_pressed()

            # Update sprites
            all_sprites.update(keys)

            # Render the screen
            self.screen.fill((135, 206, 250))  # Clear the screen with black
            all_sprites.draw(self.screen)  # Draw all sprites
            pygame.display.flip()

            # Control frame rate
            self.clock.tick(60)

        pygame.quit()
