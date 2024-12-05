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
        
        # Create platform instances as instance attributes (x,y,w,h)
        self.platform1 = World(725, 525, 250, 15)
        self.platform2 = World(0, 675, 300, 15)
        self.platform3 = World(250,600,300,15)
        self.platform4 = World(0,525,200,15)
        self.platform5 = World(0,440,50,15)
        self.platform6 = World(0,360,50,15)
        self.platform7 = World(250,400,150,15)
        self.platform8 = World(400,325,100,15)
       
        self.ground = World(0,750,1000,800)
        self.world_bound_right = World(0,0,5,800)
        self.world_bound_left = World(995,0,5,800)
        

        # Create sprite group for worlds (platforms)
        self.worlds = pygame.sprite.Group()
        self.worlds.add(self.platform1, self.platform2,self.ground,self.world_bound_right,self.world_bound_left,self.platform3,self.platform4, self.platform5,self.platform6, self.platform7,self.platform8)

    def mainloop(self):
      # Setup screen and clock
      self.screen = pygame.display.set_mode((1000, 800))
      self.clock = pygame.time.Clock()

      # Create player instance
      self.player = Player(0,750)  # Starting position near the center

      # Create sprite group for easy update and draw
      self.all_sprites = pygame.sprite.Group()
      self.all_sprites.add(self.player)
      self.all_sprites.add(self.platform1, self.platform2, self.ground, self.world_bound_right,self.world_bound_left,self.platform3,self.platform4, self.platform5,self.platform6, self.platform7,self.platform8)  # Add platforms to all_sprites

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

