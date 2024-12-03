import pygame
from src.player import Player
from src.world import World

class Controller:
    def __init__(self):
        # Initialize controller variables
        self.screen = None
        self.clock = None
        self.running = True
        self.state = "menu"
        
        # Create platform instances as instance attributes
        self.platform1 = World(400, 400, 150, 15)
        self.platform2 = World(400, 300, 150, 15)
        

        # Create sprite group for worlds (platforms)
        self.worlds = pygame.sprite.Group()
        self.worlds.add(self.platform1, self.platform2)

    def mainloop(self):
      # Setup screen and clock
      self.screen = pygame.display.set_mode((800, 600))
      self.clock = pygame.time.Clock()

      # Create player instance
      self.player = Player(375, 275)  # Starting position near the center

      # Create sprite group for easy update and draw
      self.all_sprites = pygame.sprite.Group()
      self.all_sprites.add(self.player)
      self.all_sprites.add(self.platform1, self.platform2)  # Add platforms to all_sprites

      while self.running:
          # Handle events
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  self.running = False

          # Get pressed keys
          keys = pygame.key.get_pressed()

          # Update player and platforms
          self.player.update(keys, self.worlds)  # Update player with worlds passed
          self.worlds.update()  # Update platforms 

          # Render the screen
          self.screen.fill((135, 206, 250))  # Clear the screen with color
          self.all_sprites.draw(self.screen)  # Draw all sprites
          pygame.display.flip()

          # Control frame rate
          self.clock.tick(60)

      pygame.quit()

